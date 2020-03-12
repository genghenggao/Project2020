'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-03-11 17:33:13
@LastEditors: Henggao
@LastEditTime: 2020-03-12 11:19:15
'''

import sys
import os
'''__file__获取执行文件相对路径，整行为取上一级的上一级目录'''
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from PythonDemo2020.city_country_function import get_city_country


def city_functions():
    print('请输入城市和国家，任何时候输入q退出.')
    while 1:
        city = input('Please write down your city : ')
        if city == 'q':
            break
        country = input('Please continue to input your contry : ')
        if country == 'q':
            break

    #     msg = '''
    # 城市： %s
    # 国家： %s
    #     ''' % (city, country)
    #     print(msg)
        city_country = get_city_country(city, country)
        print('You live in ' + city_country + '.')


city_functions()
