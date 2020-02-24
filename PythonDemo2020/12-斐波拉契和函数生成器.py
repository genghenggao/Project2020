'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-02-23 14:25:54
@LastEditors: Henggao
@LastEditTime: 2020-02-23 14:46:42
'''
# 0 1 1 2 3 5 8 13


def fib(n):
    a = 0
    b = 1

    count = 0
    while count < n:
        temp = a
        a = b
        b = temp + b
        # print(b)
        yield b  # 暂停
        count += 1


# fib(20)
print(fib(20))

f = fib(20)
# print(next(f))
# print(next(f))
# print("---do sth else---")
# print(next(f))
# print(f.__next__())  # 和print(next(f))一样
# print(next(f))
for f in f:
    print(f)
