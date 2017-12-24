from django.contrib.auth.models import User, Group
from models import Company, Dish, Cook
from rest_framework import viewsets
from serializers import UserSerializer, GroupSerializer, CompanySerializer, DishSerializer, CookSerializer


class UserViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class DishViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
	
class CookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Cook.objects.all()
    serializer_class = CookSerializer
