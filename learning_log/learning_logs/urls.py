'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-03-19 16:33:04
@LastEditors: Henggao
@LastEditTime: 2020-03-19 18:40:48
'''

"""定义learning_logs的URL模式"""

from django.conf.urls import url

from . import views

urlpatterns = [
    # 主页
    url(r"^$", views.index, name='index'),
    # 显示所有的主题
    url(r'^topics/$',views.topics,name="topics"),
    # 特定主题的详细页面
    url(r'^topics/(?P<topic_id>\d+)/$',views.topic,name="topic")

]
