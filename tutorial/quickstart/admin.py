# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
# Register your models here.

from models import Implementation

admin.site.register(Implementation)

from models import Course

admin.site.register(Course)

from models import Curriculum

admin.site.register(Curriculum)

from models import Degreeprogram

admin.site.register(Degreeprogram)

from models import Group

admin.site.register(Group)

from models import Unit

admin.site.register(Unit)

from models import User

admin.site.register(User)

from models import UserImplementation

admin.site.register(UserImplementation)

from models import UsersDegreeprogram

admin.site.register(UsersDegreeprogram)