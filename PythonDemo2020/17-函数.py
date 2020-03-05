'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-02-28 17:51:56
@LastEditors: Henggao
@LastEditTime: 2020-03-01 16:23:35
'''

'''
Demo1
'''
# def make_shirt(size,color):
#     print("your clothes is " + size + ", it's color is " + color+ ".")

# make_shirt("small","black")

'''
Demo 2
'''
# def build_person(first_name, last_name, age=''):
#     """返回一个字典，其中包含有关一个人的信息"""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person


# # musician = build_person('jimi', 'hendrix', age=27)
# musician = build_person('jimi', 'hendrix')
# print(musician)


'''
Demo 3
'''

# magicians = ["Tom","Jack","Tonny"]
# complete_magicians = []
# while magicians:
#     current_magician = magicians.pop()
#     complete_magicians.append(current_magician)

# print("\nThe following is magician :")
# for magician in complete_magicians:
#     print(magician)


'''
Demo 4
'''
# def show_magicians(names):
#     for name in names:
#         print("Hello, " + name.title())

# magicians = ["jack", "tom", "tonny"]
# show_magicians(magicians)


'''
Demo 4
'''


# magicians = ["jack", "tom", "tonny"]
# complete_magicians = []


# def show_magicians(names):
#     for name in names:
#         print("Hello, " + name.title())


# def make_great(names):
#     while magicians:
#         current_magician = "The Great " + magicians.pop()
#         print(current_magician)
#         complete_magicians.append(current_magician)


# make_great(magicians[:])
# magicians = complete_magicians
# print(magicians)
# show_magicians(magicians)
# show_magicians(magicians[:])


'''
Demo 5
'''


def set_cars(first, last, **other_info):

    car_info = {}
    car_info["first_name"] = first
    car_info["last_name"] = last

    for key, value in other_info.items():
        car_info[key] = value

    return car_info

finish_car = set_cars('bwd','baoma',location = "beijing",price="mid")
print(finish_car)