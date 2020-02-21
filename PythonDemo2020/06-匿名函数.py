'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-02-20 17:12:23
@LastEditors: Henggao
@LastEditTime: 2020-02-20 17:22:25
'''
def calculate(x):
    return x**2

m = calculate(2)
print(m)

# 等价于匿名函数
n = lambda y:y**2

print(n(2))


def calc(x):
    return x**2

# res = map(calc,[1,2,3,4])
res = map(lambda x:x**2,[1,2,3,4])
for i in res:
    print(i)