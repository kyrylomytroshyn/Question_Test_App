import json

from channels.db import database_sync_to_async
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from rest_framework import permissions
from .serializers import (
    TestSerializer,
    QuestionSerializer,
    UserSerializer,
    GroupSerializer,
    TestTopSerializer
)
from polls.models import Test, Question, Comment
from rest_framework import mixins
from .permissions import UserActive
from .filters import TestFilterSettings
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet



class TestViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [UserActive]
    ordering_fields = ['created_at', 'title']
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    filterset_class = TestFilterSettings

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TestViewSetTop(mixins.ListModelMixin,
                     generics.GenericAPIView):
    queryset = Test.objects.all()
    serializer_class = TestTopSerializer
    permission_classes = [UserActive]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class TestViewSetTop3(TestViewSetTop):
    queryset = Test.objects.all().order_by('-count_of_runs')[:3]


class TestViewSetForEach(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by("-id")
    serializer_class = QuestionSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
