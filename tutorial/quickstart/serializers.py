from django.contrib.auth.models import User, Group
from models import Company, Dish,Cook
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('url', 'name', 'address')

class DishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dish
        fields = ('url', 'name', 'origin')

class CookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cook
        fields = ('url', 'name', 'experience')