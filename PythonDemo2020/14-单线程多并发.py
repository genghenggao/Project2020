'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-02-23 15:42:15
@LastEditors: Henggao
@LastEditTime: 2020-02-23 15:54:34
'''


def consumer(name):
    print("------消费者%s开始吃包子了......" % name)
    while True:
        baozi = yield  # 接受外面的包子
        print("消费者%s接收到的包子编号： %s" % (name, baozi))


c1 = consumer("c1")
c2 = consumer("c2")
c3 = consumer("c3")

c1.__next__()  # 调用生成器，同时会发送到yield
c2.__next__()
c3.__next__()

for i in range(10):
    print("--------生产了第%s批包子----------")
    c1.send(i)  # 调用生成器，同时发送i
    c2.send(i)
    c3.send(i)
