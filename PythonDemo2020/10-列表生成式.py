'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-02-23 13:22:52
@LastEditors: Henggao
@LastEditTime: 2020-02-23 13:28:33
'''
a = [1, 2, 3, 4, 5, 6]

a = list(map(lambda i: i+1, a))
print(a)
# 列表生成式
b = [i + 2 for i in a]
print(b)
