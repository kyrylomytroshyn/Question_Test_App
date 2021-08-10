from django.test import TestCase, Client
from django.urls import reverse
from ..models import (
    Test,
    TestRun,
    TestQuestions,
    AnsweredTestQuestions,
    Question
)
import json


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('tests:index')
        self.detail_url = reverse('tests:test_details', args=[1, ])
        self.completed_url = reverse('tests:test_results')
        self.completed_detail_url = reverse('tests:test_results_info', args=[1, ])
        self.thanks_url = reverse('tests:thanks')
        self.search_url = reverse('tests:search-text')
        self.find_by_date_url = reverse('tests:find_by_date')

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

    def test_projects_list_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tests/index.html')

    def test_completed_list_GET(self):
        response = self.client.get(self.completed_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tests/results.html')

    def test_completed_details_GET(self):
        response = self.client.get(self.completed_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tests/result_info.html')

    def test_test_view(self):
        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tests/detail_test.html')

        self.client.post(self.detail_url, {'name': 'john'})

        self.assertEquals(TestRun.objects.count(), 2)

    def test_thanks_view(self):
        response = self.client.get(self.thanks_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tests/thanks.html')

    def test_date_view(self):
        response = self.client.get(self.find_by_date_url,  {'date_from': '2021-07-01', 'date_to': '2021-08-13'},)
        self.assertContains(response, 'Test 1')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tests/search_result.html')

    def test_search_view(self):
        response = self.client.get(self.search_url,  {'search_text': 'Test 1'},)
        self.assertContains(response, 'Test 1')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tests/search_result.html')
