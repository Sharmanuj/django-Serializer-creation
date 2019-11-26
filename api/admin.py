# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
admin.site.register(Topic)
admin.site.register(Profile)
admin.site.register(FavoriteTopics)

# Register your models here.
