"""
title = ''
author = 'huifenghechang'
mtime = '2024/4/19'
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
Python--界面UI控制，模拟键鼠操作的模块pyautogui

主要功能
鼠标操作：PyAutoGUI可以模拟鼠标移动、点击、拖拽等操作，可以控制鼠标的位置和点击的坐标。
键盘操作：PyAutoGUI可以模拟键盘按键和组合键的操作，如按下和释放按键、输入文本等。
屏幕操作：PyAutoGUI集成了pyscreeze模块，可以直接调用函数截屏、查找指定图像的位置等
延时控制：PyAutoGUI可以控制鼠标和键盘操作的延时，以确保操作的正确性和稳定性。
窗口控制：PyautoGUI集成了pygetwindow模块，可以直接调用函数获取窗口信息、控制窗口大小、移动、关闭等
"""
import pyautogui

"""
基础功能
"""
# 1.获取鼠标当前位置
print(pyautogui.position()) # Point(x=1964, y=1338)

# 2.获取屏幕大小
print(pyautogui.size())

# 3.判断坐标是否在屏幕中
print(pyautogui.onScreen(200, 200))
print(pyautogui.onScreen(2000, 4000))



"""
GUI控制功能
"""
# 自动防故障功能
# 默认这项功能为True，意味着：当鼠标的指针在屏幕的最坐上方，程序会报错；目的是为了防止程序无法停止
print(pyautogui.FAILSAFE)
pyautogui.FAILSAFE = False
print(pyautogui.FAILSAFE)


# 停顿功能
# 这个停顿只是在用pyautogui控制鼠标和键盘时生效，如果是执行一般功能的命令，则该停顿不生效
pyautogui.PAUSE = 5
pyautogui.moveTo(200, 200, duration=1);pyautogui.moveTo(2000, 1000, duration=1)



"""
鼠标控制功能
"""
#  控制移动鼠标
#  1.移动到指定位置
pyautogui.moveTo(100,300,duration=1)  #（100,300）是坐标， duration 的作用是设置移动时间，单位秒，所有的gui函数都有这个参数，而且都是可选参数 相对移动，按方向移动

# 2.相对移动，按方向移动
pyautogui.moveRel(100,500,duration=4)  # 第一个参数是左右移动像素值，第二个是上下移动像素值


# 控制鼠标点击
# 1.单击鼠标
pyautogui.click(10, 10)  # 鼠标点击指定位置，默认左键
pyautogui.click(10, 10, button='left')  # 单击左键
pyautogui.click(1000, 300, button='right')  # 单击右键
pyautogui.click(1000, 300, button='middle')  # 单击中间

# 2.双击鼠标
pyautogui.doubleClick(10,10)  # 指定位置，双击左键
pyautogui.rightClick(10,10)  # 指定位置，双击右键
pyautogui.middleClick(10,10)  # 指定位置，双击中键


# 3.按下和释放分解：点击&释放
pyautogui.mouseDown()
pyautogui.mouseUp()  # 两句命令相当于pyautogui.press()

pyautogui.mouseDown(button='right')  # 按下右键
pyautogui.mouseUp(button='right', x=100, y=200)  # 移动到（100,200），释放右键



#  控制鼠标拖动
# 1.拖动到指定位置
pyautogui.dragTo(100,300,duration=1)  # 将鼠标拖动到指定的坐标


# 2.拖动到相对位置，按方向拖动
pyautogui.dragRel(100,500,duration=4)  # 第一个参数是左右移动像素值，第二个是上下移动像素值， 向右拖动100px，向下拖动500px, 这个过程持续 4 秒钟



# 控制鼠标滚动
# 控制鼠标滚动的函数是scroll()， 传入一个整数的参数，说明向上或向下滚动多少个单位；单位根据操作系统不同而不同

pyautogui.scroll(300)  # scroll up 300 "clicks"
pyautogui.scroll(10)  # scroll up 10 "clicks"
pyautogui.scroll(10, x=100, y=100)  # move mouse cursor to 100, 200, then scroll up 10 "clicks"


# 补间/缓动函数（import Pytweening）
# 指示鼠标移动到目标位置时的进度，可以使鼠标移动变得更漂亮




"""
键盘控制功能
"""
# 按键
pyautogui.press('enter')  # 按enter键，并释放
pyautogui.press('f1')
pyautogui.press(['left', 'left', 'left'])
pyautogui.press('left', presses=3)  # 可以设置按键次数


# 组合按键，按下&释放
# 例如：要在按住 Shift 键的同时按向左箭头键
pyautogui.keyDown('shift')  # 按下shift键
pyautogui.press('left')  # 按左键，并释放
pyautogui.keyUp('shift')   # 释放shift键


# 输入字符串
pyautogui.write('Hello world!', interval=0.25)  # interval 每个字符输入间隔时间


# hold()上下文管理器
with pyautogui.hold('shift'):
    pyautogui.press(['left','left','left'])


# 热键hotkey()函数
# hotkey()可以传递多个按键字符串，这些按键字符串将按顺序按下，然后按相反的顺序释放

pyautogui.hotkey('ctrl', 'shift', 'esc')
# 相当于以下代码
# pyautogui.keyDown('ctrl')
# pyautogui.keyDown('shift')
# pyautogui.keyDown('esc')
# pyautogui.keyUp('esc')
# pyautogui.keyUp('shift')
# pyautogui.keyUp('ctrl')



"""
消息框功能
"""
# 警报框
pyautogui.alert(text='This is an alert box', title='Test', button='OK')   # 显示一个简单的消息框，其中包含文本和一个“确定”按钮。返回button键的值。


# 确认框/选择框
pyautogui.confirm('选择一项', buttons=['A', 'B', 'C'])
pyautogui.confirm(text='', title='', buttons=['OK', 'N'])   # 显示一个选择框，有多个按键，返回按键的值


# 提示输入框
pyautogui.prompt(text='', title='' , default='')
# 显示带有文本输入的消息框以及“确定”和“取消”按钮。返回输入的文本，如果单击“取消”，则返回None


# 密码输入框
pyautogui.password(text='', title='', default='', mask='*')
# 显示带有文本输入的消息框以及“确定”和“取消”按钮。键入的字符显示为*。返回输入的文本，如果单击“取消”，则返回None



"""
桌面截图，图片匹配，像素点RGB信息
"""
# 1.截图功能
pyautogui.screenshot("C:\\Users\\XX\\test.png")
# 全屏截图，传递一个文件名字符串会将截图保存到一个文件中，并将其作为一个Image对象返回。

pyautogui.screenshot("C:\\Users\\XX\\test.png", region=(0, 0, 300, 400))
# 非全屏截图，可选的region关键字参数。可以传递一个包含要捕获区域的左、顶、宽、高的四个整数元组


# 2.图片匹配
# 加载模板图像和要搜索的大图像
needleImage = pyautogui.locateOnScreen('needle.png')
haystackImage = pyautogui.screenshot()

# 查找屏幕上所有匹配位置
matches = pyautogui.locateAllOnScreen(needleImage)

pyautogui.locateAll(needleImage, haystackImage, grayscale=None, region=None)
# # 返回一个生成器，用tuple转换一下生成器，得到一个元组，元组中的每个元素是BOX类的实例对象，未匹配到则返回空元组

pyautogui.locate(needleImage, haystackImage)
# 返回值就是上图的b[0]，即BOX类的一个实例对象，如果未匹配则报异常

minSearchTime = 1
pyautogui.locateAllOnScreen(needleImage, minSearchTime)
# 与locateAll()相比第二个参数变成了minSearchTime，可以理解最小匹配时间，会在这个时间中一直从当前界面找needleImage图，直至找到返回，返回值与pyautogui.locateAll一样，是返回一个生成器

pyautogui.locateOnScreen(needleImage, minSearchTime)
# 返回值是BOX类的一个实例对象，如果未匹配则报异常

pyautogui.locateCenterOnScreen(needleImage)
# 匹配失败返回异常，匹配成功返回一个Point类的一个实例，实例属性x, y坐标，匹配到的图片中心点

# 要查找的模板图像
image = 'needle.png'
# 目标窗口的标题
title = '目标窗口标题'
pyautogui.locateOnWindow(image, title)
# 里面使用了pygetwindow模块，匹配title的UI界面中是否包含image，返回值同pyautogui.locateOnScreen


# 3.像素点RGB信息
pyautogui.center((10, 10, 6, 8))
# Point(x=13, y=14)
# 返回一个Point类的一个实例，tuple转换后为一个元组

x=13
y=14
pyautogui.pix(x, y)
# 返回屏幕像素在x, y处的颜色作为RGB元组，每种颜色表示从0到255。(x,y)像素点的（r, g, b）

# pyautogui.pixelMatchesColor(x, y, (r, g, b))
pyautogui.pixelMatchesColor(200, 500, (60, 63, 65))
# 返回True or False，即像素点的颜色匹配是否一致



"""
窗口控制功能
PyautoGUI集成了pygetwindow模块，可以直接调用函数获取窗口信息、控制窗口大小、移动、关闭等
"""
# 1.获得窗口对象
# 获得当前活动(聚焦)窗口的对象
pyautogui.getActiveWindow()  # 返回当前活动(聚焦)窗口的对象

#  获得所有可见窗口的窗口对象列表
pyautogui.getAllWindows()  # 返回所有可见窗口的窗口对象列表

# 获得当前活动(聚焦)窗口的标题
pyautogui.getActiveWindowTitle()   # 返回当前活动(聚焦)窗口的标题

#  获得所有可见窗口的标题字符串列表
pyautogui.getAllTitles()  # 返回所有可见窗口的标题字符串列表

#  获得标题文本中包含字符'ibox'的窗口对象列表
pyautogui.getWindowsWithTitle('ibox')   # 返回标题文本中包含子字符'ibox'的窗口对象列表。

# 获得包含坐标点的窗口对象列表
pyautogui.getWindowsAt(2000, 2000)   # 返回一个窗口对象列表，这些窗口包含坐标(2000, 2000)


# 2.控制窗口
# 窗口对象的属性

win = pyautogui.getWindowsWithTitle('Untitled')[0]  # win是title是'Untitled'的窗口对象

# 窗口对象的属性
win.size  # （132,100）返回元组，窗口大小
win.width  # 返回int，窗口的宽度
win.height  # 返回int，窗口的高度
win.topleft  # （10,10）返回元组，窗口最左上角坐标
win.bottomright  # （200,200）返回元组，窗口最右下角坐标
win.top  # 返回int，窗口上边缘的y坐标值
win.left  # 返回int，窗口左边缘的x坐标值
win.isMaximized  # 返回bool，窗口是否是最大窗口
win.isMinimized  # 返回bool，窗口是否是最小窗口


# 窗口对象的方法

win = pyautogui.getWindowsWithTitle('Untitled')[0]  # win是title是'Untitled'的窗口对象

# 窗口对象的方法
win.maximize()  # 窗口最大化
win.minimize()  # 窗口最大化
win.restore()  # 恢复窗口大小
win.resize(200, 200)  # 窗口x轴增加200，y轴增加200
win.resizeTo(200, 200)  # 窗口变化至x轴宽度200，y轴宽度200
win.move(10, 10)  # 窗口相对当前位置x轴移动10，y轴移动10
win.moveTo(10, 10)  # 窗口移动至10，y轴移动至10，左上角坐标（10,10）



































