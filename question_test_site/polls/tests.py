# from rest_framework.test import APITestCase
# from django.test import Client
# from django.urls import reverse
# from rest_framework import status
# from model_bakery import baker
#
# from .models import Test
#
#
# class APIQuizTest(APITestCase):
#     def setUp(self):
#         super().setUp()
#         self.url = reverse('test_list')
#         baker.make(Test, _quantity=10)
#
#     def _send_get(self):
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         return response.json()
#
#     def test_get_list(self):
#         result = self._send_get()
#         self.assertEqual(10, len(result))
