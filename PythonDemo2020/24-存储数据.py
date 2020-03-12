'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-03-06 14:21:36
@LastEditors: Henggao
@LastEditTime: 2020-03-09 15:40:59
'''

'''
Demo1 
'''
# import json
# numbers = [2, 3, 5, 7, 11, 13,15]
# filename = 'pythondemo2020/numbers.json'
# with open(filename, 'w') as f_obj:
#     json.dump(numbers, f_obj)

'''
Demo2-1
'''
# import json

# filename = 'pythondemo2020/favorite_data.json'
# favorite_data = input("Please write  your favorite number : ")
# with open(filename,'w') as f :
#     json.dump(favorite_data,f)

'''
Demo2-2
'''
# import json

# filename = 'pythondemo2020/favorite_data.json'
# with open(filename) as f:
#     num = json.load(f)
#     print('I know your favorite number! It’s ' + num + '.')


'''
Demo2-3
'''




import json
def get_data():
    filename = 'pythondemo2020/favorite_data.json'
    try:
        with open(filename, 'r') as f:
            num = json.load(f)
            # print('your favorite number is :' + num +'.')
    except FileNotFoundError:
        return None
    else:
        return num


def get_new_data():
    filename = 'pythondemo2020/favorite_data.json'
    your_favourite_data = input("Please write  your favorite number : ")
    with open(filename, 'w') as f:
        json.dump(your_favourite_data, f)
        return your_favourite_data


def prove_data():
    # num1 = input("input your number : ")
    num = get_data()
    if num:
        print('Data from get_data.Your favorite number is : ' + num + '.')

    else:
        num2 = get_new_data()
        print('Add new Data.Your favorite number is : ' + num2 + '.')


prove_data()
