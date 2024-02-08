"""
title = ''
author = 'huifenghechang'
mtime = '2023/12/27'
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
filecmp模块比较文件和目录
filecmp是python内置的一个模块，用于比较文件及文件夹的内容。

filecmp有两个主要的方法：
filecmp.cmp(f1, f2, [shallow])
filecmp.cmpfiles(a, b, common, [shallow])

filecmp.cmp(f1, f2, [shallow])，用于比较两个文件。f1、f2是文件名称，shallow为可选参数，
指定比较文件时是否需要考虑文件本身的属性，默认是True
"""

import filecmp


"""
说明：text.txt和text1.txt内容不相同，text.txt和text2.txt内容相同。
"""
res1 = filecmp.cmp("text.txt", "text1.txt", shallow=True)
print("text.txt与text1.txt的比较结果是：{}".format(res1))

res2 = filecmp.cmp("text.txt", "text2.txt", shallow=True)
print("text.txt与text2.txt的比较结果是：{}".format(res2))




























