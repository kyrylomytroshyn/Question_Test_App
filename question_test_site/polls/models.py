from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=300)
    question_number = models.IntegerField()
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Question List'
        verbose_name_plural = 'Question List'


class Test(models.Model):
    title = models.CharField(max_length=100, unique=True)
    test_info = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    questions = models.ManyToManyField(Question, through='TestQuestions')

    class Meta:
        ordering = ["-updated_at"]
        verbose_name = 'Tests'
        verbose_name_plural = 'Tests'

    def __str__(self):
        return self.title


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

    class Meta:
        verbose_name = 'Test questions'
        verbose_name_plural = 'Test questions'

