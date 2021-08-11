from datetime import datetime

from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=300)

    def __str__(self):
        return self.question

    def get_name(self):
        return self.question

    class Meta:
        verbose_name = 'Question List'
        verbose_name_plural = 'Question List'


class Test(models.Model):
    title = models.CharField(max_length=100, unique=True)
    test_info = models.TextField()
    author = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    questions = models.ManyToManyField(Question, through='TestQuestions')
    count_of_runs = models.IntegerField(default=0)


    class Meta:
        ordering = ["created_at"]
        verbose_name = 'Tests'
        verbose_name_plural = 'Tests'

    def __str__(self):
        return self.title

    def get_tests(self):
        self.question_set.all()


class TestQuestions(models.Model):
    test = models.ForeignKey(Test,
                             on_delete=models.CASCADE,
                             null=True,
                             default=None,
                             related_name='test')
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,
                                 null=True,
                                 default=None,
                                 related_name='questions')

    question_number = models.IntegerField(null=True)
    answer = models.CharField(max_length=200, unique=False, null=True)

    class Meta:
        verbose_name = 'Test questions'
        verbose_name_plural = 'Test questions'
        ordering = ["question_number"]


class AnsweredTestQuestions(models.Model):
    test = models.ForeignKey("TestRun",
                             on_delete=models.CASCADE,
                             null=True,
                             default=None,
                             related_name='answered_test')
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,
                                 null=True,
                                 default=None,
                                 related_name='answered_questions')

    question_number = models.IntegerField(null=True)
    answer = models.CharField(max_length=200, unique=False, null=True)

    class Meta:
        verbose_name = 'Test answer'
        verbose_name_plural = 'Test answers'

    def __str__(self):
        return str(self.question) + ": " + str(self.answer)


class TestRun(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)  # ForeignKey(User, on_delete=models.CASCADE)
    count_of_questions = models.IntegerField(null=True)
    count_of_created_questions = models.IntegerField(null=True)
    questions = models.ManyToManyField(Question, through=AnsweredTestQuestions)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.test)
