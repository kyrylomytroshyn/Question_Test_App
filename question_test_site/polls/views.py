from django.shortcuts import render, redirect
from .models import Test, Question, TestRun, AnsweredTestQuestions, TestQuestions
from django.views.generic import ListView


class TestListView(ListView):
    model = Test
    context_object_name = "tests"
    template_name = "tests/index.html"


def tests_view(request, pk):
    test = TestRun.objects.get(test_id=pk)
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
    list_of_answers = []
    count_of_questions = 0

    if request.method == 'POST':

        for i in range(len(questions)):
            ans = request.POST['ans' + str(i+1)]
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
    return render(request, 'tests/thanks.html')
