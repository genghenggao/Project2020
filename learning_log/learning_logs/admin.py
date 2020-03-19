'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-03-18 18:25:39
@LastEditors: Henggao
@LastEditTime: 2020-03-19 13:23:11
'''
from django.contrib import admin

# Register your models here.

from learning_logs.models import Topic,Entry


admin.site.register(Topic)
admin.site.register(Entry)
