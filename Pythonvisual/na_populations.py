'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-03-17 14:56:06
@LastEditors: Henggao
@LastEditTime: 2020-03-17 15:06:22
'''
import pygal

wm = pygal.maps.world.World()
wm.title = "Population of Countreis in North America"
wm.add('North America', {'ca': 24126000, 'us': 30934900, 'mx': 113423000})

wm.render_to_file('na_populations.svg')
