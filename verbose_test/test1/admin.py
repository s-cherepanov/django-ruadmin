# -*- coding: utf-8 -*-

from django.contrib import admin
from test1.models import *



class TestCaseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter  = ('name',)
    
class TestCaseAdminOld(admin.ModelAdmin):
    list_display = ('name',)    
    list_filter  = ('name',)

admin.site.register(TestCase, TestCaseAdmin)
admin.site.register(TestCaseOld, TestCaseAdminOld)

