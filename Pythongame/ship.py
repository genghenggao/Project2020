'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-03-13 16:08:04
@LastEditors: Henggao
@LastEditTime: 2020-03-13 16:23:43
'''
import pygame


class Ship():

    def __init__(self, screen):
        '''初始化'飞船并设置其初始化位置'''
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('Python游戏开发/img/ship.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放置在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)
