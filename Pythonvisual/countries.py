'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-03-17 13:55:32
@LastEditors: Henggao
@LastEditTime: 2020-03-17 14:07:55
'''
from pygal_maps_world.i18n import COUNTRIES

for countru_code in sorted(COUNTRIES.keys()):
    print(countru_code,COUNTRIES[countru_code])