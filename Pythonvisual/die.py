'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-03-16 14:26:34
@LastEditors: Henggao
@LastEditTime: 2020-03-16 14:29:30
'''

from random import randint

class Die():
    '''表示一个骰子的类'''

    def __init__(self,num_sides=6):
        ''''骰子默认为6面'''
        self.num_sides =num_sides

    def roll(self):
        '''返回一个位于1和投资面之间的随机值'''
        return randint(1,self.num_sides)
