# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Company(models.Model):
	name = models.CharField(max_length=45)
	address = models.CharField(max_length=45)
	
	def __str__(self):
		return self.name

class Dish(models.Model):
	name = models.CharField(max_length=45)
	origin = models.CharField(max_length=45)
	
	def __str__(self):
		return self.name

class Cook(models.Model):
    name = models.CharField(max_length=45)
    experience = models.CharField(max_length=45)

    def __str__(self):
        return self.name
