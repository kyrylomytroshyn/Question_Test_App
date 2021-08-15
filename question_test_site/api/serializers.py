from polls.models import Test, Question
from rest_framework import serializers
from django.contrib.auth.models import User, Group


class TestSerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.CharField()  # validators=[title_has_digits]
    created_at = serializers.DateTimeField(format='iso-8601', read_only=True)

    class Meta:
        model = Test
        fields = ['title', 'test_info', 'author', 'questions', 'count_of_runs', 'created_at']


class TestTopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Test
        fields = ['title', 'count_of_runs']


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['question']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
