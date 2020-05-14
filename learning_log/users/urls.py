'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-04-22 12:53:37
@LastEditors: Henggao
@LastEditTime: 2020-04-22 20:03:37
'''
'''为应用程序users定义url模式'''

# from django.contrib.auth import login

from . import views
from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
app_name = 'users'
urlpatterns = [
    # 登录界面
    # url(r'^login/$', login,
    #     {'template_name': 'users/login.html'}, name='login'),
    url(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
    # 注销
    url(r'^login/$', LogoutView.as_view(), name='logout'),
    # # Registration page.
    # path('register/', views.register, name='register'),
    # 注册页面
    url(r'^register/$', views.register, name='register'),
]
