"""
title = ''
author = 'huifenghechang'
mtime = '2024/2/6'
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
异常处理
"""

# 捕获指定异常
try:
    print(name)
    1 / 0
except NameError as e:
    print("出现了异常")
    print(e)  # name 'name' is not defined


# 捕获所有异常
try:
    1 / 0
except Exception as e:
    print("出现异常")

# 异常的传递
def func1():
    print("func1开始执行")
    num = 1 / 0
    print("func1结束执行")

def func2():
    print("func1开始执行")
    func1()
    print("func1结束执行")

def main():
    try:
        func2()
    except Exception as e:
        print(f"出现异常了，异常的信息是{e}")  # 出现异常了，异常的信息是division by zero

main()
