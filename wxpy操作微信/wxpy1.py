"""
title = ''
author = 'huifenghechang'
mtime = '2024/1/14'
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
wxpy模块
"""
# 机器人对象
# —登录和初始化

from wxpy import *
def login():
    print('状态:登录成功  ',end='')
def login_out():
    print('微信已退出!')
bot=Bot(login_callback=login,logout_callback=login_out,cache_path='login.pkl',qr_path='login_qr.png')
print('当前用户:'+bot.self.name)
bot.auto_mark_read()# 自动清除手机端消息红点提示
bot.enable_puid(path='wxpy_puid.pkl')# 启用puid属性 具有稳定性的标识
bot = Bot(console_qr=True, cache_path=True)

# 给机器人自己发送消息
bot.self.send('Hello World!')
# 给文件传输助手发送消息
bot.file_helper.send('Hello World!')

