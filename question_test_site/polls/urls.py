from django.urls import path

from .views import (
    TestListView,
    tests_view,
    test_results,
    test_results_info,
    TestRunView,
test_run
)

app_name = 'tests'

urlpatterns = [
    path('', TestListView.as_view(), name="index"),
    #path('add', views.TestAddView.as_view(), name="add_test"),
    path('<int:pk>', test_run, name="test_details"),
    path('completed', test_results, name="test_results"),
    path('completed/<int:pk>', test_results_info, name="test_results_info")
]
