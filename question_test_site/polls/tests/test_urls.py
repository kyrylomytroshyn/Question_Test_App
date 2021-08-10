from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import (
    TestListView,
    test_results,
    test_results_info,
    test_run,
    thanks,
    search,
    find_by_date
)


class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('tests:index')
        self.assertEquals(resolve(url).func.view_class, TestListView)

    def test_results_url_is_resolved(self):
        url = reverse('tests:test_results')
        self.assertEquals(resolve(url).func, test_results)

    def test_result_info_url_is_resolved(self):
        url = reverse('tests:test_results_info', args=[1, ])
        self.assertEquals(resolve(url).func, test_results_info)

    def test_test_run_is_resolved(self):
        url = reverse('tests:test_details', args=[1, ])
        self.assertEquals(resolve(url).func, test_run)

    def test_thanks_url_is_resolved(self):
        url = reverse('tests:thanks')
        self.assertEquals(resolve(url).func, thanks)

    def test_search_url_is_resolved(self):
        url = reverse('tests:search-text')
        self.assertEquals(resolve(url).func, search)

    def test_find_by_date_url_is_resolved(self):
        url = reverse('tests:find_by_date')
        self.assertEquals(resolve(url).func, find_by_date)