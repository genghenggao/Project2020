'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-03-13 15:17:47
@LastEditors: Henggao
@LastEditTime: 2020-03-15 19:18:15
'''
import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # 初始化游戏，创建一个屏幕对象
    pygame.init()
    # screen = pygame.display.set_mode((1200, 800))
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption('Alien Invasion')

    # 设置背景
    # bg_color= (230,230,230)
    # 创建一艘飞船
    ship = Ship(screen)

    # 开始游戏的主循环
    while True:

        # 监听键盘和鼠标事件
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        gf.check_events()

        # 每次循环都重新绘制屏幕
        # screen.fill(bg_color)
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
