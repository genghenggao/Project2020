'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-03-27 16:21:01
@LastEditors: Henggao
@LastEditTime: 2020-03-27 18:21:39
'''
import os

# 列出vedio目录下所有的文件
# files = os.listdir('.')  # 如果path为None，则使用path = '.'
files = os.listdir('./video')  # 如果path为None，则使用path = '.'

for filename in files:
    portion = os.path.splitext(filename)  # 分离文件名与扩展名
    # 如果后缀是jpg
    if portion[1] == '.MP4':
        # 指定的路径
        os.chdir('./video')
        # 重新组合文件名和后缀名
        newname = portion[0] + '.mp4'
        os.rename(filename, newname)
