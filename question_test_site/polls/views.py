# from django.forms import formset_factory
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, Http404, get_object_or_404
#
from django.urls import reverse_lazy
from django.views import View

#from .forms import RunForm, CategoriaModelForm
from .models import Test, Question, TestRun, AnsweredTestQuestions, TestQuestions
# from questions.models import Question
# from django.views import View
# from .forms import RunForm
from django.views.generic import ListView, DetailView, UpdateView


# from django.urls import reverse_lazy
# from .forms import PostForm
# from django.forms.models import modelform_factory, inlineformset_factory
#
#
class TestListView(ListView):
    model = Test
    context_object_name = "tests"
    template_name = "tests/index.html"


def tests_view(request, pk):
    test = TestRun.objects.get(test_id=pk)
    # for i in test.questions.all():
    #     print("-------------" + str(i.question))
    if request.method == "POST":
        pass
    else:
        context = {'form': test}
        return render(request, 'tests/detail_test.html', context)


def test_results(request):
    """Getting test results headers into template 'tests/results'"""
    results = TestRun.objects.all()
    context = {'form': results}
    return render(request, 'tests/results.html', context)


def test_results_info(request, pk):
    results_info = AnsweredTestQuestions.objects.filter(test_id=pk)
    context = {'form': results_info}
    return render(request, 'tests/result_info.html', context)


def test_run(request, pk):
    test = Test.objects.get(id=pk)
    questions = TestQuestions.objects.filter(test_id=pk)
    # form = CategoriaModelForm(instance=test)
    # model = inlineformset_factory(Test, Test.questions.through, exclude=['id',] )
    # #results_info = get_object_or_404(TestQuestions, test_id=pk)

    if request.method == 'POST':
        pass
    else:
        context = {
            'form': test,
            'questions': questions,
        }
        #questions = AnsweredTestQuestions.objects.get(pk=pk)
        # form = CategoriaModelForm(instance=results_info)
    #     formset = model(instance=test)
    #
    # context = {'form': form,
    #            'formset': formset}
    return render(request, 'tests/detail_test.html', context)


#

class TestRunView(View):
#    test_to_show = get_object_or_404(TestRun, pk=pk)
    model = TestRun
    form_class = AnsweredTestQuestions

    def get(self, request, *args, **kwargs):
        form = RunForm()
        questions = TestRun.objects.create()
        context = {"form": form, "questions": questions}
        return render(request, "tests/detail_test.html", context)

    def post(self, request):
        form = RunForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy(''))  # HttpResponseRedirect('/posts/')
        context = {"form": form}
        return render(request, "tests/add_test.html", context)
    # test = Test.objects.get(pk=pk)
    # questions = []
    # for q in test.get_question():
    #     ans == []
    #     for a in q.
# class TestDetailView(DetailView):
#     model = Test
#     context_object_name = "test_details"
#     template_name = "tests/detail_test.html"
#
#
# class TestAddView(View):
#
#     def get(self, request):
#         form = PostForm()
#         context = {"form": form}
#         return render(request, "tests/add_test.html", context)
#
#     def post(self, request):
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse_lazy(''))  # HttpResponseRedirect('/posts/')
#         context = {"form": form}
#         return render(request, "tests/add_test.html", context)
#
#
# class TestRunView(DetailView):
#
#     def get(self, request, *args, **kwargs):
#         form = PostForm()
#         context = {"form": form}
#         return render(request, "tests/add_test.html", context)
#
#     def post(self, request):
#         return render(request, "tests/thanks.html")
#
#
# def create_test(request, pk):
#     """ Create classes view """
#     # my_form = modelform_factory(TestQuestions, ["test", "question"])
#     my_form = inlineformset_factory(Test, TestQuestions, fields=['question'])
#
#     if request.method == "POST":
#         form = my_form(request.POST)
#         if form.is_valid():
#             stock = form.save(commit=False)
#             stock.professor_id = request.user
#             stock.save()
#             return redirect("tests/thanks.html")
#     else:
#         form = my_form()
#
#     return render(
#         request,
#         "tests/add_test.html",
#         {"title": "Create Classes", "form": form},
#     )
#
#
# # def test_profile_settings(request):
# #     """
# #     Allows a user to update their own profile.
# #     """
# #
# #     # Create the formset, specifying the form and formset we want to use.
# #     LinkFormSet = formset_factory(AddQuestion)
# #
# #     # # Get our existing link data for this user.  This is used as initial data.
# #     # user_links = UserLink.objects.filter(user=user).order_by('anchor')
# #     # link_data = [{'anchor': l.anchor, 'url': l.url}
# #     #                 for l in user_links]
# #
# #     if request.method == 'POST':
# #         profile_form = AddTest(request.POST)
# #         link_formset = LinkFormSet(request.POST)
# #
# #         if profile_form.is_valid() and link_formset.is_valid():
# #             # Save user info
# #             user.first_name = profile_form.cleaned_data.get('first_name')
# #             user.last_name = profile_form.cleaned_data.get('last_name')
# #             user.save()
# #
# #             # Now save the data for each form in the formset
# #             new_links = []
# #
# #             for link_form in link_formset:
# #                 anchor = link_form.cleaned_data.get('anchor')
# #                 url = link_form.cleaned_data.get('url')
# #
# #                 if anchor and url:
# #                     new_links.append(UserLink(user=user, anchor=anchor, url=url))
# #
# #
# #
# #     else:
# #         profile_form = ProfileForm(user=user)
# #         link_formset = LinkFormSet(initial=link_data)
# #
# #     context = {
# #         'profile_form': profile_form,
# #         'link_formset': link_formset,
# #     }
# #
# #     return render(request, 'our_template.html', context)
