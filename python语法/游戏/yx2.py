"""
title = ''
author = 'huifenghechang'
mtime = '2024/1/5'
code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
┏┓      ┏┓
┏┛┻━━━┛┻┓
┃      ☃      ┃
┃  ┳┛  ┗┳  ┃
┃      ┻      ┃
┗━┓      ┏━┛
┃      ┗━━━┓
┃  神兽保佑    ┣┓
┃　永无BUG！   ┏┛
┗┓┓┏━┳┓┏┛
┃┫┫  ┃┫┫
┗┻┛  ┗┻┛
"""
"""
贪吃蛇
1. 案例介绍

贪吃蛇是一款经典的益智游戏，简单又耐玩。该游戏通过控制蛇头方向吃蛋，从而使得蛇变得越来越长。
通过上下左右方向键控制蛇的方向，寻找吃的东西，每吃一口就能得到一定的积分，而且蛇的身子会越吃
越长，身子越长玩的难度就越大，不能碰墙，不能咬到自己的身体，更不能咬自己的尾巴，等到了一定的分
数，就能过关，然后继续玩下一关。本例难度为中级，适合具有 Python 基础和 Pygame 编程知识的用
户学习。

2. 设计要点

游戏是基于 PyGame 框架制作的，程序核心逻辑如下：游戏界面分辨率是 640*480，蛇和食物都是由
 1 个或多个 20*20 像素的正方形块儿(为了方便，下文用点表示 20*20 像素的正方形块儿) 组成，
 这样共有 32*24 个点，使用 pygame.draw.rect 来绘制每一个点；初始化时蛇的长度是 3，食物是
  1 个点，蛇初始的移动的方向是右，用一个数组代表蛇，数组的每个元素是蛇每个点的坐标，因此数组的
  第一个坐标是蛇尾，最后一个坐标是蛇头；游戏开始后，根据蛇的当前移动方向，将蛇运动方向的前方的
  那个点 append 到蛇数组的末位，再把蛇尾去掉，蛇的坐标数组就相当于往前挪了一位；如果蛇吃到了
  食物，即蛇头的坐标等于食物的坐标，那么在第 2 点中蛇尾就不用去掉，就产生了蛇长度增加的效果；
  食物被吃掉后，随机在空的位置(不能与蛇的身体重合) 再生成一个；通过 PyGame 的 event 监控按
  键，改变蛇的方向，例如当蛇向右时，下一次改变方向只能向上或者向下；当蛇撞上自身或墙壁，游戏结束
  ，蛇头装上自身，那么蛇坐标数组里就有和舌头坐标重复的数据，撞上墙壁则是蛇头坐标超过了边界，
  都很好判断；其他细节：做了个开始的欢迎界面；食物的颜色随机生成；吃到实物的时候有声音提示等
"""
import pygame
from os import path
from sys import exit
from time import sleep
from random import choice
from itertools import product
from pygame.locals import QUIT, KEYDOWN


def direction_check(moving_direction, change_direction):
    directions = [['up', 'down'], ['left', 'right']]
    if moving_direction in directions[0] and change_direction in directions[1]:
        return change_direction
    elif moving_direction in directions[1] and change_direction in directions[0]:
        return change_direction
    return moving_direction


class Snake:
    colors = list(product([0, 64, 128, 192, 255], repeat=3))[1:-1]

    def __init__(self):
        self.map = {(x, y): 0 for x in range(32) for y in range(24)}
        self.body = [[100, 100], [120, 100], [140, 100]]
        self.head = [140, 100]
        self.food = []
        self.food_color = []
        self.moving_direction = 'right'
        self.speed = 4
        self.generate_food()
        self.game_started = False

    def check_game_status(self):
        if self.body.count(self.head) > 1:
            return True
        if self.head[0] < 0 or self.head[0] > 620 or self.head[1] < 0 or self.head[1] > 460:
            return True
        return False

    def move_head(self):
        moves = {
            'right': (20, 0),
            'up': (0, -20),
            'down': (0, 20),
            'left': (-20, 0)
        }
        step = moves[self.moving_direction]
        self.head[0] += step[0]
        self.head[1] += step[1]

    def generate_food(self):
        self.speed = len(
            self.body) // 16 if len(self.body) // 16 > 4 else self.speed
        for seg in self.body:
            x, y = seg
            self.map[x // 20, y // 20] = 1
        empty_pos = [pos for pos in self.map.keys() if not self.map[pos]]
        result = choice(empty_pos)
        self.food_color = list(choice(self.colors))
        self.food = [result[0] * 20, result[1] * 20]


def main():
    key_direction_dict = {
        119: 'up',  # W
        115: 'down',  # S
        97: 'left',  # A
        100: 'right',  # D
        273: 'up',  # UP
        274: 'down',  # DOWN
        276: 'left',  # LEFT
        275: 'right',  # RIGHT
    }

    fps_clock = pygame.time.Clock()
    pygame.init()
    pygame.mixer.init()
    snake = Snake()
    sound = False
    if path.exists('eat.wav'):
        sound_wav = pygame.mixer.Sound("eat.wav")
        sound = True
    title_font = pygame.font.SysFont('simsunnsimsun', 32)
    welcome_words = title_font.render(
        '贪吃蛇', True, (0, 0, 0), (255, 255, 255))
    tips_font = pygame.font.SysFont('simsunnsimsun', 20)
    start_game_words = tips_font.render(
        '点击开始', True, (0, 0, 0), (255, 255, 255))
    close_game_words = tips_font.render(
        '按ESC退出', True, (0, 0, 0), (255, 255, 255))
    gameover_words = title_font.render(
        '游戏结束', True, (205, 92, 92), (255, 255, 255))
    win_words = title_font.render(
        '蛇很长了，你赢了！', True, (0, 0, 205), (255, 255, 255))
    screen = pygame.display.set_mode((640, 480), 0, 32)
    pygame.display.set_caption('贪吃蛇')
    new_direction = snake.moving_direction
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key == 27:
                    exit()
                if snake.game_started and event.key in key_direction_dict:
                    direction = key_direction_dict[event.key]
                    new_direction = direction_check(
                        snake.moving_direction, direction)
            elif (not snake.game_started) and event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 213 <= x <= 422 and 304 <= y <= 342:
                    snake.game_started = True
        screen.fill((255, 255, 255))
        if snake.game_started:
            snake.moving_direction = new_direction  # 在这里赋值，而不是在event事件的循环中赋值，避免按键太快
            snake.move_head()
            snake.body.append(snake.head[:])
            if snake.head == snake.food:
                if sound:
                    sound_wav.play()
                snake.generate_food()
            else:
                snake.body.pop(0)
            for seg in snake.body:
                pygame.draw.rect(screen, [0, 0, 0], [
                    seg[0], seg[1], 20, 20], 0)
            pygame.draw.rect(screen, snake.food_color, [
                snake.food[0], snake.food[1], 20, 20], 0)
            if snake.check_game_status():
                screen.blit(gameover_words, (241, 310))
                pygame.display.update()
                snake = Snake()
                new_direction = snake.moving_direction
                sleep(3)
            elif len(snake.body) == 512:
                screen.blit(win_words, (33, 210))
                pygame.display.update()
                snake = Snake()
                new_direction = snake.moving_direction
                sleep(3)
        else:
            screen.blit(welcome_words, (240, 150))
            screen.blit(start_game_words, (246, 310))
            screen.blit(close_game_words, (246, 350))
        pygame.display.update()
        fps_clock.tick(snake.speed)


if __name__ == '__main__':
    main()
