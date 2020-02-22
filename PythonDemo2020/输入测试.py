'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-02-20 18:31:50
@LastEditors: Henggao
@LastEditTime: 2020-02-21 13:28:12
'''

import random

n = random.randint(0, 100)

user_guess = int(input("input your guess : "))

if user_guess > n:
    print("try smaller")
elif user_guess < n:
    print("try bigger")
else:
    print("Bingo ,you get it")

print(n)