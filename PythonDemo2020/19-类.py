'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-03-01 16:53:07
@LastEditors: Henggao
@LastEditTime: 2020-03-05 13:40:38
'''

'''
Demo 1
'''

# class Dog():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def run(self):
#         print(self.name.title() + ' is now running')

#     def sit(self):
#         print(self.name.title() + ' is now sitting')


# my_dog = Dog('willie', 6)
# print("My dog's name is " + my_dog.name.title() + ".")
# print("My dog is " + str(my_dog.age) + " years old.")
# my_dog.sit()
# my_dog.run()


'''
Demo 2 
'''


# class Restaurant():

#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         print("The restaurant is called " + self.restaurant_name.title() + '.')
#         print("The restaurant's type is " + self.cuisine_type + '.')

#     def open_restaurant(self):
#         print("The restaurant is open.")

# my_restaurant = Restaurant("henggao","delicious")
# your_restaurant = Restaurant("brill","more delicious")

# my_restaurant.describe_restaurant()
# your_restaurant.describe_restaurant()


'''
Demo 3
'''


# class Car():
#     """一次模拟汽车的简单尝试"""

#     def __init__(self, make, model, year):
#         """初始化描述汽车的属性"""
#         self.make = make
#         self.model = model
#         self.year = year

#     def get_descriptive_name(self):
#         """返回整洁的描述性信息"""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()


# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())


'''
Demo 4
'''

class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

class ElectricCar(Car):

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        super().__init__(make, model, year)
        self.price = 20

my_electriccar = ElectricCar('awd', 'b5', 2020)
print(my_electriccar.price)