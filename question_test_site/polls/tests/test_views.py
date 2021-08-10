from django.test import TestCase, Client
from django.urls import reverse
from ..models import (
    Test,
    TestRun,
    TestQuestions,
    AnsweredTestQuestions,
    Question
)

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('tests:index')
        self.detail_url = reverse('tests:test_details', args=[1,])

    def test_projects_list_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tests/index.html')

