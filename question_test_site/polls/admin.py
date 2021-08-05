from django.contrib import admin
from .models import Test, Question, TestQuestions, TestRun, AnsweredTestQuestions
from django.urls import reverse


class TestQuestionInline(admin.TabularInline):
    model = TestQuestions

class AnsweredQuestionInline(admin.TabularInline):
    model = AnsweredTestQuestions

class TestAdmin(admin.ModelAdmin):
    model = Test
    list_display = ('title', 'created_at', 'category_post_count')

    inlines = [
        TestQuestionInline
    ]

    def category_post_count(self, obj):
        return obj.questions.count()

    category_post_count.short_description = "Count of questions"

class AnswerListAdmin(admin.ModelAdmin):
    model = AnsweredTestQuestions
    list_display = ("test", "question", "answer")

class TestRunAdmin(admin.ModelAdmin):
    model = TestRun

    inlines = [
        AnsweredQuestionInline
    ]


admin.site.register(Test, TestAdmin)
admin.site.register(Question)
admin.site.register(TestRun, TestRunAdmin)
admin.site.register(AnsweredTestQuestions, AnswerListAdmin)