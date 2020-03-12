'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-03-12 20:58:23
@LastEditors: Henggao
@LastEditTime: 2020-03-12 22:01:04
'''
import sys
import os
'''__file__获取执行文件相对路径，整行为取上一级的上一级目录'''
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from PythonDemo2020.employee import Employee
import unittest

class TestSalary(unittest.TestCase):

    def setUp(self):

        self.my_employee = Employee('lebron','james',3500)

    def test_give_default_raise(self):

        name =  self.my_employee.first_name.title() + ' ' + self.my_employee.last_name.title()
        test_salary =  self.my_employee.give_raise()
        print('=====默认增加5000=====')
        print(name + ' :\t' + str(test_salary))

    def test_give_custom_raise(self):

        print('=====自定义增加=====')
        name =  self.my_employee.first_name.title() + ' ' + self.my_employee.last_name.title()
        test_salary = self.my_employee.give_raise(6000)

        print(name + ' :\t' + str(test_salary))


unittest.main()
