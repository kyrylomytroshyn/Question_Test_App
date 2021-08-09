from django.shortcuts import render, redirect
from .models import Test, TestRun, AnsweredTestQuestions, TestQuestions
from django.views.generic import ListView
from django.utils.translation import gettext as _
import logging

app_log = logging.getLogger("tests_app")


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


def tests_view(request, pk):
    app_log.info(f"Request: Get test number {pk}")
    test = TestRun.objects.get(test_id=pk)
    context = {'form': test}
    return render(request, 'tests/detail_test.html', context)


def test_results(request):
    """Getting test results headers into template 'tests/results'"""
    app_log.info(f"Request: Get test results")
    results = TestRun.objects.all()
    context = {'form': results}
    return render(request, 'tests/results.html', context)


def test_results_info(request, pk):
    app_log.info(f"Request: Get test result number {pk}")
    results_info = AnsweredTestQuestions.objects.filter(test_id=pk)
    context = {'form': results_info}
    return render(request, 'tests/result_info.html', context)


def test_run(request, pk):
    app_log.info(f"Request: Start test number {pk}")
    test = Test.objects.get(id=pk)
    questions = TestQuestions.objects.filter(test_id=pk)
    list_of_answers = []
    count_of_questions = 0

    if request.method == 'POST':

        for i in range(len(questions)):
            ans = request.POST['ans' + str(i + 1)]
            list_of_answers.append(ans)
            if len(ans) != 0:
                count_of_questions += 1
        newpost = TestRun(test=test,
                          user=request.POST['name'],
                          count_of_questions=count_of_questions)
        newpost.save()

        for q in questions:
            newpost.questions.add(q.question)

        manyquestions = AnsweredTestQuestions.objects.filter(test_id=newpost.id)
        for i in range(len(manyquestions)):
            manyquestions[i].answer = list_of_answers[i]
            manyquestions[i].save()

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
        tests = Test.objects.filter(title__contains=searched)
        context = {'searched': searched,
                   'tests': tests}
        app_log.info(f"Request: Get info from {searched}")
        return render(request, "tests/search_result.html", context)

    return render(request, "tests/search_result.html", {})


def find_by_date(request):
    if request.method == "GET":
        searched_from = request.GET['date_from']
        searched_to = request.GET['date_to']
        res = Test.objects.filter(created_at__range=[searched_from, searched_to])

        context = {'tests': res,
                   'searched': f"period from {searched_from} to {searched_to}"}
        app_log.info(f"Request: Find tests with period from {searched_from} to {searched_to}. "
                      f"Result: {res}")
        return render(request, "tests/search_result.html", context)

    return render(request, "tests/search_result.html", {})
