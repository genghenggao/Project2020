'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-02-20 17:25:29
@LastEditors: Henggao
@LastEditTime: 2020-02-20 17:46:30
'''
def get_abs(n):
    return abs(n)

def add(x,y,f):
    return f(x) + f(y)

print(add(2,-10,get_abs))