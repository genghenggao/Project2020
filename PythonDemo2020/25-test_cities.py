'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-03-11 17:22:11
@LastEditors: Henggao
@LastEditTime: 2020-03-12 12:10:18
'''
import sys
import os
#  __file__获取执行文件相对路径，整行为取上一级的上一级目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from PythonDemo2020.city_country_function import get_city_country
import unittest

class NameTestCase(unittest.TestCase):
    '''测试city_country.py'''

    def test_city_country(self):
        '''显示城市和国家'''
        show_city_country = get_city_country('beijing', 'China')

    def test_city_country_population(self):
        show_city_country = get_city_country('beijing', 'China',200000)


unittest.main()
