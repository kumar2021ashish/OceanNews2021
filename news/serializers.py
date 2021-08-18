from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

from rest_framework import status
from rest_framework.response import Response




class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','url', 'username', 'email']


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id','usernews','author','title','description','imageurl','publishdate']

