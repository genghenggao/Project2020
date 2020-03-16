'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-03-13 16:46:16
@LastEditors: Henggao
@LastEditTime: 2020-03-14 16:29:13
'''
import sys

import pygame

def check_event():
    '''相应案件和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()