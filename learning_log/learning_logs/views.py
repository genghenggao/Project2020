'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-03-18 18:25:39
@LastEditors: Henggao
@LastEditTime: 2020-03-19 18:38:51
'''
from django.shortcuts import render

from .models import Topic

# Create your views here.


def index(request):
    """学习笔记主页"""
    return render(request, "learning_logs/index.html")


def topics(request):
    """显示所有主题"""
    topics = Topic.objects.order_by("date_added")
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request,topic_id):
    """显示单个主题及其所有的条目"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic,'entries':entries}
    return render(request,'learning_logs/topic.html',context)