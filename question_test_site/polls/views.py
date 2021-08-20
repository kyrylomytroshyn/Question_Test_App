from django.http import HttpResponseRedirect, HttpResponse
from django.utils import translation
from django.shortcuts import render, redirect
from .models import Test, TestRun, AnsweredTestQuestions, TestQuestions
from django.views.generic import ListView
from django.utils.translation import LANGUAGE_SESSION_KEY
import logging
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.cache import cache
from question_test_site import settings

app_log = logging.getLogger("tests_app")

CACHE_TIME = 60 * 10  # 60 seconds * 10 = 10 minutes
MIN_CACHE_TIME = 60 * 10  # 60 seconds * 10 = 10 minutes


class TestListView(ListView):
    model = Test
    context_object_name = "tests"
    template_name = "tests/index.html"
    app_log.info(f"Request: GET TEST LIST")

    def get_queryset(self):
        filter_val = self.request.GET.get('order', 'up')
        if filter_val == "up":
            val = ""
        else:
            val = "-"
        app_log.info(f"Request: SORT BY {filter_val}")
        new_context = Test.objects.all().order_by(val + 'title')
        return new_context

    def get_context_data(self, **kwargs):
        context = super(TestListView, self).get_context_data(**kwargs)
        context['order'] = self.request.GET.get('order', 'give-default-value')
        return context


# def tests_view(request, pk):
#     app_log.info(f"Request: Get test number {pk}")
#
# cache_name = 'test_view' + str(pk)
# test = cache.get(cache_name)
# print(test)
# if not test:
#     test = TestRun.objects.get(test_id=pk)
#     cache.set(cache_name, test, CACHE_TIME)
#
# context = {'form': test}
# return render(request, 'tests/detail_test.html', context)


@login_required(login_url='/accounts/login')
def test_results(request):
    """Getting test results headers into template 'tests/results'"""
    app_log.info(f"Request: Get test results")
    results = TestRun.objects.filter(user=request.user)
    context = {'form': results}

    return render(request, 'tests/results.html', context)


@login_required(login_url='/accounts/login')
def test_results_info(request, pk):
    app_log.info(f"Request: Get test result number {pk}")

    cache_name = 'test_view_results' + str(pk)
    results_info = cache.get(cache_name)

    if not results_info:
        results_info = AnsweredTestQuestions.objects.filter(test_id=pk)
        cache.set(cache_name, results_info, CACHE_TIME)
    context = {'form': results_info}
    return render(request, 'tests/result_info.html', context)


@login_required(login_url='/accounts/login/')
def test_run(request, pk):
    app_log.info(f"Request: Start test number {pk}")

    cache_name_test = 'test_run_test' + str(pk)
    cache_name_questions = 'test_run_quest' + str(pk)
    test = cache.get(cache_name_test)
    questions = cache.get(cache_name_questions)
    if not test:
        test = Test.objects.get(id=pk)
        cache.set(cache_name_test, test, CACHE_TIME)
    if not questions:
        questions = TestQuestions.objects.filter(test_id=pk)
        cache.set(cache_name_questions, questions, CACHE_TIME)

    list_of_answers = []
    count_of_questions = 0

    if request.method == 'POST':
        count_of_questions_to_pass = len(questions)
        for i in range(count_of_questions_to_pass):
            ans = request.POST['ans' + str(i + 1)]
            list_of_answers.append(ans)
            if len(ans) != 0:
                count_of_questions += 1
        newpost = TestRun(test=test,
                          user=request.user,
                          count_of_questions=count_of_questions,
                          count_of_created_questions=count_of_questions_to_pass)
        newpost.save()

        if count_of_questions_to_pass == count_of_questions:
            test.count_of_runs += 1
            test.save()

        for q in questions:
            newpost.questions.add(q.question)

        manyquestions = AnsweredTestQuestions.objects.filter(test_id=newpost.id)
        for i in range(len(manyquestions)):
            manyquestions[i].answer = list_of_answers[i]
            manyquestions[i].save()
        app_log.info(f"Request: Completed new Test Run. "
                     f"Completed {count_of_questions} of {count_of_questions_to_pass}")
        return redirect('/thanks')
    context = {
        'form': test,
        'questions': questions,
    }

    return render(request, 'tests/detail_test.html', context)


def thanks(request):
    app_log.info(f"Request: Get test 'thanks' overlay ")
    return render(request, 'tests/thanks.html')


def search(request):
    if request.method == "POST":
        searched = request.POST['search_text']
        if searched == "":
            return redirect('/')
        cache_name = 'search=' + str(searched)
        tests = cache.get(cache_name)

        if not tests:
            tests = Test.objects.filter(title__contains=searched)
            cache.set(cache_name, tests, CACHE_TIME)

        context = {'searched': searched,
                   'tests': tests}
        app_log.info(f"Request: Get info from {searched}")
        return render(request, "tests/search_result.html", context)

    return render(request, "tests/search_result.html", {})


def find_by_date(request):
    if request.method == "GET":
        searched_from = request.GET['date_from']
        searched_to = request.GET['date_to']
        cache_name = 'search=' + str.join(str(searched_from), str(searched_from))
        res = cache.get(cache_name)

        if not res:
            res = Test.objects.filter(created_at__range=[searched_from, searched_to])
            cache.set(cache_name, res, CACHE_TIME)

        context = {'tests': res,
                   'searched': f"period from {searched_from} to {searched_to}"}
        app_log.info(f"Request: Find tests with period from {searched_from} to {searched_to}. "
                     f"Result: {res}")
        return render(request, "tests/search_result.html", context)

    return render(request, "tests/search_result.html", {})


def register_request(request):
    if request.user.is_authenticated:
        return redirect('/')
    form_register = NewUserForm()
    if request.method == "POST":
        form_register = NewUserForm(request.POST)
        if form_register.is_valid():
            user = form_register.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('/')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    return render(request=request, template_name="registration/register.html", context={"register_form": form_register})


def login_request(request):
    login_form = AuthenticationForm()
    if request.POST == "POST":
        login_form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Wrong pass or login.")
    return render(request, 'registration/login.html', {'form': login_form})


def lang(request, lang_code):
    go_next = request.META.get('HTTP_REFERER', '/')
    response = HttpResponseRedirect(f"/{lang_code}")
    # if lang_code and translation.check_for_language(lang_code):
    #     if hasattr(request, 'session'):
    #         request.session['django_language'] = lang_code
    #         request.session['_language'] = lang_code
    #     else:
    #         response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
    #     translation.activate(lang_code)
    # return response
    # go_next = request.META.get('HTTP_REFERER', '/')
    # response = HttpResponseRedirect(go_next)
    if hasattr(request, 'session'):
        request.session[LANGUAGE_SESSION_KEY] = lang_code
    else:
        response.set_cookie(
            settings.LANGUAGE_COOKIE_NAME, lang_code,
            max_age=settings.LANGUAGE_COOKIE_AGE,
            path=settings.LANGUAGE_COOKIE_PATH,
            domain=settings.LANGUAGE_COOKIE_DOMAIN,
        )
    return response


def switch_lang(request):
    return render(request, 'tests/langswitch.html')

# def switch_lang(request, code):
#     go_next = request.META.get('HTTP_REFERER', '/')
#     response = HttpResponseRedirect(go_next)
#     if code and translation.check_for_language(code):
#         if hasattr(request, 'session'):
#             print(request.session['django_language'])
#             print(request.session['_language'])
#             request.session['django_language'] = code
#             request.session['_language'] = code
#         else:
#             response.set_cookie(settings.LANGUAGE_COOKIE_NAME, code)
#         translation.activate(code)
#     return response
