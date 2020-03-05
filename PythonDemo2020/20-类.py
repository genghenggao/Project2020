'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-03-03 15:39:25
@LastEditors: Henggao
@LastEditTime: 2020-03-05 13:47:40
'''
from collections import OrderedDict

favorite_languages = OrderedDict()
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
    language.title() + ".")