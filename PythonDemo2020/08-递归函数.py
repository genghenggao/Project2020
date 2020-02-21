'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-02-20 17:52:06
@LastEditors: Henggao
@LastEditTime: 2020-02-20 18:04:08
'''
# 循环
n = 100
 
while n > 0 :
    n = int(n / 2)
    print(n)

# 函数递归
def calc(n):
    print(n)
    n = int(n / 2)
    if n > 0:
        calc(n)

    print(n)
    
calc(100)