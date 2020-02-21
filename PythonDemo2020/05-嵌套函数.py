'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-02-20 16:48:55
@LastEditors: Henggao
@LastEditTime: 2020-02-20 17:04:39
'''
name = " 全局name"
def change():
    name = " change name"

    def change2():
        name = "change2 name"
        print("第三层打印 " + name)
    change2()
    print("第二层打印 " + name)

change()
print("最外层打印 " + name)