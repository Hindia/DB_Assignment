#from django.contrib.auth.models import User, Group
from models import Implementation, Course,Curriculum, Degreeprogram, Group, Unit, User, UserImplementation, UsersDegreeprogram
from rest_framework import viewsets
from tutorial.quickstart.serializers import ImplementationSerializer, CourseSerializer,CurriculumSerializer, DegreeprogramSerializer, GroupSerializer, UnitSerializer, UserSerializer, UserImplementationSerializer, UsersDegreeprogramSerializer

class ImplementationViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows users to be viewed or edited.
    """ 
    queryset = Implementation.objects.all()
    serializer_class = ImplementationSerializer

class CourseViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows groups to be viewed or edited.
    """ 
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CurriculumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer

class DegreeprogramViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = Degreeprogram.objects.all()
    serializer_class = DegreeprogramSerializer
	
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
	
class UnitViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
	
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
	
class UserImplementationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = UserImplementation.objects.all()
    serializer_class = UserImplementationSerializer
	
class UsersDegreeprogramViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = UsersDegreeprogram.objects.all()
    serializer_class = UsersDegreeprogramSerializer
