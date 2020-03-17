'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-03-17 14:25:06
@LastEditors: Henggao
@LastEditTime: 2020-03-17 14:51:19
'''
import pygal

# wm = pygal.Worldmap()
wm = pygal.maps.world.World()
wm.title = "North, Center, and South America"

wm.add("North America", ['ca', 'mx', 'us'])
wm.add("Center America", ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add("South America", ['ar', 'bo', 'br', 'cl', 'co', 'ec',
                         'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])
wm.render_to_file('americas.svg')
