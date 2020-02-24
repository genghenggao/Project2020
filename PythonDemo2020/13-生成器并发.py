'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-02-23 15:19:45
@LastEditors: Henggao
@LastEditTime: 2020-02-23 15:48:31
'''


def g_test():
    while True:
        n = yield  # 接收到的值给n
        print("receive from outside : ", n)


g = g_test()
g.__next__()  # 调用生成器，同时会发送None到yield

for i in range(10):
    g.send(i)  # 调用生成器，同时发送i
