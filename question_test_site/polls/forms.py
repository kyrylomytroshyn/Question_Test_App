from django import forms
from django.forms import formset_factory
from .models import Test, TestRun  # , Question, TestQuestions


#
# class PostForm(forms.ModelForm):
#     title = forms.CharField(
#         label="Title",
#         widget=forms.TextInput(attrs={"class": "form-control"}),
#         required=True,
#     )
#     test_info = forms.CharField(
#         label="Info",
#         widget=forms.Textarea(attrs={"class": "form-control"}),
#         required=True,
#     )
#     author = forms.CharField(
#         label="Author name",
#         widget=forms.TextInput(attrs={"class": "form-control"}),
#         required=True,
#     )
#
#     questions = forms.ModelMultipleChoiceField(
#         label="Questions",
#         queryset=Question.objects.all(),
#         widget=forms.CheckboxSelectMultiple()
#     )
#     class Meta:
#         model = Test
#         fields = ("title", "test_info", "author", "questions")
#
#
# from question_test_site.polls.models import Test


# class RunForm(forms.ModelForm):
#     title = forms.CharField(
#         label="Title",
#         widget=forms.TextInput(),
#     )
#     user = forms.CharField(
#         label="User name",
#         widget=forms.Textarea(),
#     )
#
#     # questions = forms.MultiValueField(
#     #     label="Questions",
#     #     queryset=TestRun.objects.all,
#     #     widget=forms.TextInput()
#     # )
#
#     class Meta:
#         model = Test
#         fields = ("title", "user", "questions")
#
#
# class CategoriaModelForm(forms.ModelForm):
#     class Meta:
#         model = Test
#         exclude = ('id',)
