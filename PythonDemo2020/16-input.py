'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-02-27 16:26:05
@LastEditors: Henggao
@LastEditTime: 2020-02-28 17:30:21
'''
'''
Demo 1
'''
# name = input("Please write your name : ")
# print(name)

'''
Demo 2
'''
# name = ''
# # name = input("Please write your friend's name : ")
# name = ''
# while name != "jack":
#     name = input("Please write your friend's name : ")
#     print("Hello , " + name.title())

'''
Demo3
 1、    age<3        free   
 2、    3<=age<=12   10
 3、    age > 12     15
'''
# age = True
# while age:
#     age = int(input("Please tell me your age :"))
#     if age < 3:
#         print("Free")
#     elif 3 <= age <= 12:
#         print("price is 10")
#     else:
#         print("price is 15")


'''
Demo4
'''
info= {}
active = True
while active:
    name = input("What's your name :")
    place = input("\nwhere do you want to go")

    info[name] = place

    repeate = input("Do you want to add others ? (yes/no)")
    if repeate =='no':
        active = False

print("\n------ All Info------")
for name,place in info.items():
    print(name.title() + " want to go to " + place.title() + '.')