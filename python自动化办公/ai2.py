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
自动截图和图像识别
"""

import pyautogui

# 截图并保存
pyautogui.screenshot('screenshot.png')

# 假设我们需要找到屏幕上的某个特定图标并点击它
# 首先，截取那个图标的图片，命名为"icon.png"

# 使用locateCenterOnScreen找到屏幕上的图标位置
icon_location = pyautogui.locateCenterOnScreen('icon.png')

# 如果找到了图标，移动鼠标并双击它
if icon_location:
    pyautogui.moveTo(icon_location)
    pyautogui.doubleClick()
