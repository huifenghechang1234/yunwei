"""
title = ''
author = 'huifenghechang'
mtime = '2024/4/5'
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
生成器
"""

# 使用函数创建生成器
# def fib(max):
#     a, b = 1, 1
#     while a < max:
#         yield a  # generators return an iterator that returns a stream of values.
#         a, b = b, a + b
#
#
# for n in fib(15):
#     print(n)



g = (i * 3 if i < 10 else i * 5 for i in range(100))
print(next(g))
print(next(g))