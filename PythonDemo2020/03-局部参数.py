'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-02-20 16:17:05
@LastEditors: Henggao
@LastEditTime: 2020-02-20 16:32:45
'''
name = "henggao"
def change():
    name = "Brill"
    print(name)
    print(locals())
    print(globals())
    
change() 

print(name)