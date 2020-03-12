'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-03-06 12:28:21
@LastEditors: Henggao
@LastEditTime: 2020-03-06 14:21:05
'''

'''
Demo 1
'''
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")


'''
Demo2
'''
# def message_counts(filename):
    
#     try:
#         with open(filename,'r') as f:
#             contents = f.read()
#     except FileNotFoundError: 
#         msg = "Sorry, the file " + filename + " does not exist."
#         print(msg)
#     else:
#         # 计算文件大致包含多少个单词
#         words = contents.split()
#         num_words = len(words)
#         print("The file " + filename + " has about " + str(num_words) +
#         " words.")

# # filename = 'alice.txt'
# # filename = 'PythonDemo2020/guest.txt'
# # message_counts(filename)
# filenames = ['PythonDemo2020/guest.txt',
#             'PythonDemo2020/programming.txt', 
#             'PythonDemo2020/pi_digits.txt', 
#             'PythonDemo2020/guest_book1.txt']
# for filename in filenames:
#     message_counts(filename)

