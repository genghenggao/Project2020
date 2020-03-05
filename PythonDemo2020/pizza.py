'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-03-01 16:26:54
@LastEditors: Henggao
@LastEditTime: 2020-03-01 16:31:59
'''

def make_pizza(color,size,*toppings):
    print("color : " + color + "\nsize : " + size )

    for topping in toppings:
        print("\n-" + topping)