#from django.contrib.auth.models import User, Group
from models import Implementation, Course,Curriculum, Degreeprogram, Group, Unit, User, UserImplementation, UsersDegreeprogram
from rest_framework import serializers

class ImplementationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Implementation
        fields = ('url', 'impcode', 'courseid')

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('url', 'coursename', 'credithours', 'curriculumid')

class CurriculumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Curriculum
        fields = ('url', 'code', 'module_name', 'year', 'groupid', 'degreeprogramid')

class DegreeprogramSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Degreeprogram
        fields = ('url', 'programcode', 'programname', 'unitid')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'groupcode', 'groupname')

class UnitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Unit
        fields = ('url', 'unitcode', 'unitname')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'firstname', 'surname', 'groupid')
		
class UserImplementationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserImplementation
        fields = ('url', 'userid', 'implementationid')
		
class UsersDegreeprogramSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UsersDegreeprogram
        fields = ('url', 'usersid', 'degreeprogramid')