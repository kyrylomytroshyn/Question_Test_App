from django.urls import path

from .views import (
    TestListView,
    test_results,
    test_results_info,
    test_run,
    thanks
)

app_name = 'tests'

urlpatterns = [
    path('', TestListView.as_view(), name="index"),
    path('<int:pk>', test_run, name="test_details"),
    path('completed', test_results, name="test_results"),
    path('completed/<int:pk>', test_results_info, name="test_results_info"),
    path('thanks', thanks, name="thanks")
]
