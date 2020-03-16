'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-03-16 15:16:12
@LastEditors: Henggao
@LastEditTime: 2020-03-16 15:59:35
'''

import sys
import os
#  __file__获取执行文件相对路径，整行为取上一级的上一级目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from Pythonvisual.die import Die
import pygal

# 创建一个D6
die = Die()

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# print(results)
# 分析结果
frequencies = []
for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)
# 对数据进行可视化
hist = pygal.Bar()

hist.title = 'Result of rolling one D6 1000 times.'
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = 'Result' 
hist.y_title = "Frequency of Result"

hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')

