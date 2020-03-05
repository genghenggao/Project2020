'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-03-05 15:27:07
@LastEditors: Henggao
@LastEditTime: 2020-03-05 18:38:45
'''

'''
Demo1
'''
# filename = 'PythonDemo2020/programming.txt'
# with open(filename, 'w') as file_object:
#     file_object.write("I love programming.")


'''
Demo2
'''
# filename = 'PythonDemo2020/guest.txt'

# name = input('Please write yuor name :')
# with open(filename,'w') as f :
#     f.writelines(name)

'''
Demo3
'''
filename = 'PythonDemo2020/guest_book.txt'
name = ''
while name != 'no':
    name = input('Please write your name : ')
    with open(filename,'a') as f :
        f.writelines(name + '\n')
        print('Hi,' + name + '. Welcome to visit my house.')