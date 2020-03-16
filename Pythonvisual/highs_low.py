'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-03-16 19:44:34
@LastEditors: Henggao
@LastEditTime: 2020-03-16 20:51:22
'''
import csv
from datetime import datetime

from matplotlib import pyplot as plt

# 从文件从获取日期、最高价格和最低价格
filename = 'price1.csv'
with open(filename, 'r') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:               
            current_date = datetime.strptime(row[4], "%Y/%m/%d")
            high = float(row[8])
            low = float(row[9])
        except ValueError:
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # print(highs)
# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red',alpha=0.5)
plt.plot(dates, lows, c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
# 设置图形的格式
title = "Daily high_low trade price, January 2015"
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Price(RMB)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
# plt.savefig('color_date_price.png', bbox_inches='tight')
