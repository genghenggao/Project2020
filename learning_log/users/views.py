'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-04-20 16:50:45
@LastEditors: Henggao
@LastEditTime: 2020-04-22 19:13:40
'''
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout

def logout_view(request):
    '''注销用户'''
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))