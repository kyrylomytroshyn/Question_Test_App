from django.contrib import admin
from .models import Question, Test, TestQuestions


class TestQuestionInline(admin.TabularInline):
    model = TestQuestions


class TestAdmin(admin.ModelAdmin):
    model = Test
    list_display = ('title', 'created_at', 'category_post_count')
    inlines = [
        TestQuestionInline
    ]

    def category_post_count(self, obj):
        return obj.questions.count()

    category_post_count.short_description = "Count of questions"


admin.site.register(Test, TestAdmin)
admin.site.register(Question)
