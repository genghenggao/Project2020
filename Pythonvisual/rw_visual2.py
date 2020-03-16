'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-03-15 19:13:54
@LastEditors: Henggao
@LastEditTime: 2020-03-16 13:32:15
'''
import sys
import os
#  __file__获取执行文件相对路径，整行为取上一级的上一级目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from Pythonvisual.random_walk import RandomWalk
import matplotlib.pylab as plt

# 只要程序处于活动状态，就不断的模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk(5000)
    rw.fill_walk()

    # 设置绘制窗口尺寸
    plt.figure(dpi=128,figsize=(10,6))

    plt.plot(rw.x_values, rw.y_values, linewidth=1)  

    # 突出起点和终点
    plt.scatter(0,0,c='green',edgecolors='none',s =100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
                    s=100)
                    
    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    plt.show()
    # 保存图片
    # plt.savefig('water_visual2.png', bbox_inches='tight')

    keep_running = input("Make anther walk? (y/n):")
    if keep_running == 'n':
        break
