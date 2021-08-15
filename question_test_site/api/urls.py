from django.urls import include, path
from rest_framework import routers
from api.views import (
    TestViewSet,
    QuestionViewSet,
    UserViewSet,
    GroupViewSet,
    TestViewSetForEach,
    TestViewSetTop3,
    TestViewSetTop
)
from rest_framework.authtoken import views
router = routers.DefaultRouter()
# router.register(r'tests', TestViewSet)
router.register(r"questions", QuestionViewSet)
router.register(r"users", UserViewSet)
router.register(r"groups", GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("api/", include("rest_framework.urls", namespace="rest_framework")),
    path("tests/", TestViewSet.as_view(), name="test_list"),
    path("tests/<int:pk>", TestViewSetForEach.as_view(), name="test_details"),
    path("tests/top-3", TestViewSetTop3.as_view(), name="test_top_3"),
    path('tests/scores', TestViewSetTop.as_view(), name="test_top"),
]
