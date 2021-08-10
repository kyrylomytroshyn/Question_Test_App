from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from rest_framework import permissions
from .serializers import (
    TestSerializer,
    QuestionSerializer,
    UserSerializer,
    GroupSerializer,
)
from polls.models import Test, Question
from rest_framework import mixins


class TestViewSet(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    # # permission_classes = [IsAdminUser]
    # @classmethod
    # def get_extra_actions(cls):
    #     return []
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


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


# class TestViewSet(mixins.ListModelMixin,
#                   generics.GenericAPIView):
#     queryset = Test.objects.all()
#     serializer_class = TestSerializer
#
#     # # permission_classes = [IsAdminUser]
#     # @classmethod
#     # def get_extra_actions(cls):
#     #     return []
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

# class TestViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     model = Test
#     queryset = Test.objects.all().order_by('-created_at')
#     serializer_class = TestSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Question.objects.all().order_by("-id")
    serializer_class = QuestionSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
