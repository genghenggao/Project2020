'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-03-15 11:43:57
@LastEditors: Henggao
@LastEditTime: 2020-03-15 15:43:52
'''
import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

# 设置图标标题，坐标加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)

# 设置刻度标记大小
plt.tick_params(axis='both', labelsize=14)

plt.show()
