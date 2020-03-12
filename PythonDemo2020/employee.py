'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-03-12 20:51:27
@LastEditors: Henggao
@LastEditTime: 2020-03-12 22:03:00
'''


class Employee():
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, rasie_salary=5000):
        '''薪资默认增加5000'''
        self.salary += int(rasie_salary)
        return self.salary

# my_employee = Employee('a','b',3000)
# print(my_employee.first_name)
# print(my_employee.last_name)
# print(my_employee.salary)
# raise_salary = my_employee.give_raise()
# print(raise_salary)
