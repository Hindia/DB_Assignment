# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-02 21:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0003_cook'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseid', models.CharField(db_column='courseID', max_length=10, unique=True)),
                ('coursename', models.CharField(db_column='courseName', max_length=50, unique=True)),
                ('credithours', models.IntegerField(db_column='creditHours')),
            ],
            options={
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(db_column='Code', max_length=10, unique=True)),
                ('module_name', models.CharField(db_column='Module Name', max_length=50)),
                ('year', models.IntegerField()),
                ('groupid', models.IntegerField()),
            ],
            options={
                'db_table': 'curriculum',
            },
        ),
        migrations.CreateModel(
            name='Degreeprogram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('programcode', models.CharField(db_column='ProgramCode', max_length=10, unique=True)),
                ('programname', models.CharField(db_column='programName', max_length=50)),
            ],
            options={
                'db_table': 'degreeProgram',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupcode', models.CharField(db_column='groupCode', max_length=10, unique=True)),
                ('groupname', models.CharField(db_column='groupName', max_length=50)),
            ],
            options={
                'db_table': 'group',
            },
        ),
        migrations.CreateModel(
            name='Implementation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('impcode', models.CharField(db_column='impCode', max_length=10, unique=True)),
                ('courseid', models.ForeignKey(db_column='courseid', on_delete=django.db.models.deletion.CASCADE, to='tutorial.Course')),
            ],
            options={
                'db_table': 'Implementation',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unitcode', models.CharField(db_column='unitCode', max_length=10, unique=True)),
                ('unitname', models.CharField(db_column='unitName', max_length=50, unique=True)),
            ],
            options={
                'db_table': 'unit',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_column='userName', max_length=7, unique=True)),
                ('firstname', models.CharField(db_column='firstName', max_length=10)),
                ('surname', models.CharField(db_column='surName', max_length=10)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Cook',
        ),
        migrations.DeleteModel(
            name='Dish',
        ),
        migrations.CreateModel(
            name='UserImplementation',
            fields=[
                ('userid', models.ForeignKey(db_column='userid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='tutorial.User')),
                ('implementationid', models.ForeignKey(db_column='Implementationid', on_delete=django.db.models.deletion.CASCADE, to='tutorial.Implementation')),
            ],
            options={
                'db_table': 'user_Implementation',
            },
        ),
        migrations.CreateModel(
            name='UsersDegreeprogram',
            fields=[
                ('usersid', models.ForeignKey(db_column='usersid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='tutorial.User')),
            ],
            options={
                'db_table': 'users_degreeProgram',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='groupid',
            field=models.ForeignKey(db_column='groupid', on_delete=django.db.models.deletion.CASCADE, to='tutorial.Group'),
        ),
        migrations.AddField(
            model_name='degreeprogram',
            name='unitid',
            field=models.ForeignKey(db_column='unitid', on_delete=django.db.models.deletion.CASCADE, to='tutorial.Unit'),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='degreeprogramid',
            field=models.ForeignKey(db_column='degreeProgramid', on_delete=django.db.models.deletion.CASCADE, to='tutorial.Degreeprogram'),
        ),
        migrations.AddField(
            model_name='course',
            name='curriculumid',
            field=models.ForeignKey(db_column='curriculumid', on_delete=django.db.models.deletion.CASCADE, to='tutorial.Curriculum'),
        ),
        migrations.AddField(
            model_name='usersdegreeprogram',
            name='degreeprogramid',
            field=models.ForeignKey(db_column='degreeProgramid', on_delete=django.db.models.deletion.CASCADE, to='tutorial.Degreeprogram'),
        ),
        migrations.AlterUniqueTogether(
            name='usersdegreeprogram',
            unique_together=set([('usersid', 'degreeprogramid')]),
        ),
        migrations.AlterUniqueTogether(
            name='userimplementation',
            unique_together=set([('userid', 'implementationid')]),
        ),
    ]
