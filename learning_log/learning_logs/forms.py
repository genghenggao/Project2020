'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-04-17 16:16:18
@LastEditors: Henggao
@LastEditTime: 2020-04-19 12:39:51
'''
from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}
        
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}