# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from models import Company

admin.site.register(Company)

from models import Dish

admin.site.register(Dish)

from models import Cook

admin.site.register(Cook)