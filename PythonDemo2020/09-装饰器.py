'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-02-22 17:57:47
@LastEditors: Henggao
@LastEditTime: 2020-02-22 21:28:18
'''
account = {
    "is_authentic": False,  # 用户登录就改成True
    "username": "henggao",  # 用户名
    "password": "abc123"  # 用户密码
}


def login(func):
    def inner(*args, **kwargs):
        if account["is_authentic"] is False:
            username = input("username :")
            password = input("password :")
            if username == account["username"] and password == account["password"]:
                print("Welcome login ...")
                account["is_authentic"] = True
                func(*args, **kwargs)  # 认证成功，执行功能函数
            else:
                print("Wrong username or passwprd")
        else:
            print("用户已登录，验证通过")
            func(*args, **kwargs)  # 认证成功，执行功能函数
    return inner


def home():
    print("-----首页-----")


@login
def book():
    # login()  # 执行前加上验证
    print("-----书籍------")


@login
def vedio(vip_level):
    if vip_level > 3:
        print("解锁新区域")
    else:
        print("-----视频专区")


home()
# book()
# login(book)
# book = login(book)  # inner的内存地址
book()  # inner()
vedio(4)
