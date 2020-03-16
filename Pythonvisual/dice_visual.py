'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-03-16 16:07:04
@LastEditors: Henggao
@LastEditTime: 2020-03-16 18:50:41
'''
import sys
import os
#  __file__获取执行文件相对路径，整行为取上一级的上一级目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import pygal
from Pythonvisual.die import Die

# c创建两个D6骰子
die_1 = Die()
die_2 = Die()

# 掷骰子多次，并将结果存储到一个列表中
# results = []
# for roll_num in range(1000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]

# 分析结果
# frequencies = []
max_result = die_1.num_sides + die_2.num_sides
# for value in range(2,max_result+1):
#     frequency = results.count(value)
#     frequencies.append(frequency)
frequencies = [results.count(value) for value in range(2,max_result)]

# 可视化结果
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times"
# hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist.x_labels = [str(x) for x in range(2, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Freauency of result"

hist.add("D6 + D6", frequencies)
hist.render_to_file('dice_visual_sum.svg')
