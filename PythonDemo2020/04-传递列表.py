'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-02-20 16:41:36
@LastEditors: Henggao
@LastEditTime: 2020-02-20 16:44:04
'''
names = ["henggao","Brill"]
def change():
    names.append("James")
    return names

change()
print(names)