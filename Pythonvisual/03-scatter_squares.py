'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-03-15 15:56:33
@LastEditors: Henggao
@LastEditTime: 2020-03-15 16:59:03
'''

import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values,
            cmap=plt.cm.Blues, edgecolors='none', s=40)

# 设置图标标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Squares of value", fontsize=14)

# 设置刻度标记的大小
# plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标的取值范围
plt.axis([0, 1100, 0, 1100000])
# plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')
