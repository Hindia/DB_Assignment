# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Implementation(models.Model):
    impcode = models.CharField(db_column='impCode', unique=True, max_length=10)  # Field name made lowercase.
    courseid = models.ForeignKey('Course', on_delete=models.CASCADE, db_column='courseid')

    class Meta:
        db_table = 'Implementation'


class Course(models.Model):
    #courseid = models.CharField(db_column='courseID', unique=True, max_length=10)  # Field name made lowercase.
    coursename = models.CharField(db_column='courseName', unique=True, max_length=50)  # Field name made lowercase.
    credithours = models.IntegerField(db_column='creditHours')  # Field name made lowercase.
    curriculumid = models.ForeignKey('Curriculum', on_delete=models.CASCADE, db_column='curriculumid')

    class Meta:
        db_table = 'course'


class Curriculum(models.Model):
    code = models.CharField(db_column='Code', unique=True, max_length=10)  # Field name made lowercase.
    module_name = models.CharField(db_column='Module Name', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    year = models.IntegerField()
    groupid = models.IntegerField()
    degreeprogramid = models.ForeignKey('Degreeprogram', on_delete=models.CASCADE, db_column='degreeProgramid')  # Field name made lowercase.

    class Meta:
        db_table = 'curriculum'


class Degreeprogram(models.Model):
    programcode = models.CharField(db_column='ProgramCode', unique=True, max_length=10)  # Field name made lowercase.
    programname = models.CharField(db_column='programName', max_length=50)  # Field name made lowercase.
    unitid = models.ForeignKey('Unit', on_delete=models.CASCADE, db_column='unitid')

    class Meta:
        db_table = 'degreeProgram'


class Group(models.Model):
    groupcode = models.CharField(db_column='groupCode', unique=True, max_length=10)  # Field name made lowercase.
    groupname = models.CharField(db_column='groupName', max_length=50)  # Field name made lowercase.

    class Meta:
        db_table = 'group'


class Unit(models.Model):
    unitcode = models.CharField(db_column='unitCode', unique=True, max_length=10)  # Field name made lowercase.
    unitname = models.CharField(db_column='unitName', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        db_table = 'unit'


class User(models.Model):
    username = models.CharField(db_column='userName', unique=True, max_length=7)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=10)  # Field name made lowercase.
    surname = models.CharField(db_column='surName', max_length=10)  # Field name made lowercase.
    groupid = models.ForeignKey(Group, on_delete=models.CASCADE, db_column='groupid')

    class Meta:
        db_table = 'user'


class UserImplementation(models.Model):
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='userid', primary_key=True)
    implementationid = models.ForeignKey(Implementation, on_delete=models.CASCADE, db_column='Implementationid')  # Field name made lowercase.

    class Meta:
        db_table = 'user_Implementation'
        unique_together = (('userid', 'implementationid'),)


class UsersDegreeprogram(models.Model):
    usersid = models.ForeignKey(User, models.DO_NOTHING, db_column='usersid', primary_key=True)
    degreeprogramid = models.ForeignKey(Degreeprogram, on_delete=models.CASCADE, db_column='degreeProgramid')  # Field name made lowercase.

    class Meta:
        db_table = 'users_degreeProgram'
        unique_together = (('usersid', 'degreeprogramid'),)
