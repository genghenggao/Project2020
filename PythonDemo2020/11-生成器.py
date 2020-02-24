'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-02-23 13:37:37
@LastEditors: Henggao
@LastEditTime: 2020-02-23 14:01:52
'''
# 引子
# 先生成后运算
for i in range(10000):  # 生成10000次
    print(i)

    if i > 100:
        break

# 一边生成一边运算
count = 0
while count < 10000:
    print(count)
    count += 1
    if count > 100:
        break

# 生成器
x = [1, 3, 4, 5, 6]
g = (i for i in x)
print(g)
print(next(g))
print(next(g))
print(next(g))

# 修改一下
x = [1, 3, 4, 5, 6]
g = (i for i in x)
for i in g:
    print(i)