"""
title = ''
author = 'huifenghechang'
mtime = '2024/4/22'
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
自动打开记事本并写入内容
"""

import pyautogui
import time

# 等待一秒，确保程序不会立即执行，给你时间切换到桌面
time.sleep(1)

# 模拟按下"Win + R"打开运行对话框
pyautogui.hotkey('win', 'r')
time.sleep(0.5)

# 在运行对话框中输入"notepad"并按回车，打开记事本
pyautogui.typewrite('notepad')
pyautogui.press('enter')

# 等待记事本打开
time.sleep(1)

# 在记事本中写入文字
pyautogui.typewrite('Hello, PyAutoGUI!')