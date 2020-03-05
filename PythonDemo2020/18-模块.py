'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-03-01 16:29:53
@LastEditors: Henggao
@LastEditTime: 2020-03-01 17:03:26
'''
import sys,os
#  __file__获取执行文件相对路径，整行为取上一级的上一级目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from PythonDemo2020 import pizza
pizza.make_pizza("white", "mid", 'green peppers', 'extra cheese')
