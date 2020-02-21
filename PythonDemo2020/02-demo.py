'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-02-18 21:58:53
@LastEditors: Henggao
@LastEditTime: 2020-02-20 16:01:45
'''
def register(name,*args,**kwargs):
    print(name,args,kwargs)
    
register("Alex",22,"Student",sex="M",address="Jiangsu")