from django.test import TestCase
from ..models import (
    Test,
    Question,
    TestRun,
    AnsweredTestQuestions,
    TestQuestions
)


class TestModels(TestCase):

    def setUp(self):
        self.first_test = Test.objects.create(
            title='Test 1',
            test_info='Hi',
            author='123'
        )

        self.first_question = Question.objects.create(
            question="how are you"
        )

        self.first_test_run = TestRun.objects.create(
            test=self.first_test,
            user='adm',
            count_of_questions=123,
        )

    def test_project_is_assigned_pk_on_creation(self):
        self.assertEquals(self.first_test.id, 1)

    def test_question_is_assigned_pk_on_creation(self):
        self.assertEquals(self.first_question.id, 1)

    def test_testrun_is_assigned_pk_on_creation(self):
        self.assertEquals(self.first_test_run.id, 1)
        self.assertEquals(self.first_test_run.test.id, 1)

        self.first_test_run.questions.add(self.first_question)
        manyquestions = AnsweredTestQuestions.objects.filter(
            test_id=self.first_test.id)
