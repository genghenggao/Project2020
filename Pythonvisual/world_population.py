'''
@Description: 
@Versiion: 1.0
@Autor: Henggao
@Date: 2020-03-17 12:40:15
@LastEditors: Henggao
@LastEditTime: 2020-03-17 15:44:46
'''
import sys
import os
#  __file__获取执行文件相对路径，整行为取上一级的上一级目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import json
from Pythonvisual.country_codes import get_country_code
import pygal
from pygal.style import LightColorizedStyle as LCS,RotateStyle as RS

# 将一个数据加载到一个列表中
filename = 'population.json'
with open(filename, 'r') as f:
    pop_data = json.load(f)
    # print(pop_data)

# 创建一个包含人口数量的字典
cc_populations = {}
# 打印每个国家2010年的人口数量
for pop_dict in pop_data:
    # print(pop_dict)
    # print(pop_dict["Country Name"])
    # print(pop_dict['Year'] == 2010)
    if pop_dict['Year'] == 2010:
        country_name = pop_dict['Country Name']
        population = int(pop_dict['Value'])
        # print(country_name + ':' + str(population))
        code = get_country_code(country_name)
        if code:
            # print(code + ':' + str(population))
            cc_populations[code] = population
        # else:
        #     print('ERROR - ' + country_name)

# 根据人口数量将所有国家分成三组
cc_pops_1, cc_pops_2, cc_pops_3 = {},{},{}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_2[cc] = pop
    elif pop < 10000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# 看看每组分别包含多少国家
print(len(cc_pops_1),len(cc_pops_2),len(cc_pops_3))

wm = pygal.maps.world.World()
wm_style = RS('#336699',base_style=LCS)
wm = pygal.maps.world.World(style=wm_style)
wm.title = "World Population in 2010, by Country"
wm.add('0-10m',cc_pops_1)
wm.add('1-1bn',cc_pops_2)
wm.add('>1bn',cc_pops_3)

wm.render_to_file('light_style_world_population.svg')