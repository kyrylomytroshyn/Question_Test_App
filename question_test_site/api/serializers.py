from polls.models import Test, Question
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .validators import title_has_digits

class TestSerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.CharField(validators = [title_has_digits])
    class Meta:
        model = Test
        fields = ['title', 'created_at']




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
