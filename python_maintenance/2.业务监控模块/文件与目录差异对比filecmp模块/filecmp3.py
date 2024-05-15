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
多目录对比， 通过 dircmp(a,b[,ignore[,hide]］）类创建一个目录比较对象 ，其中a和b
是参加比较的目录名。ignore 代表文件名忽略的列表，并 默认为 ['RCS', 'CVS', 'tags'];
hide代表隐藏的列表，默认为[os.curdir ,os.pardir] 。dircmp类可以获得目录比较的
详细信息，如只有在a 目录中包括的文件、a与b都存在的子目录、匹配的文件等，同时支待递归
"""

import filecmp

a = "K:\PythonProject\wsw1\dir1"    # 定义左目录
b = "K:\PythonProject\wsw1\dir2"  # 定义右目录
dirobj = filecmp.dircmp(a,b,['test_main.py'])   #目录比较，忽略 test_main.py 文件
# 输出对比结果数据报表，详细说明请参考filecmp 类方法及属性信息
dirobj.report()
dirobj.report_partial_closure()
dirobj.report_full_closure()
print('----------------------------------------------------------')
print("left_list;" + str(dirobj.left_list))
print('----------------------------------------------------------')
print("right_list:" + str(dirobj.right_list))
print('----------------------------------------------------------')
print("common:" + str(dirobj.common))
print('----------------------------------------------------------')
print("left_only:" + str(dirobj.left_only))
print('----------------------------------------------------------')
print("right_only:" + str(dirobj.right_only))
print('----------------------------------------------------------')
print("common_dirs:" + str(dirobj.common_dirs))
print('----------------------------------------------------------')
print("common_files:" + str(dirobj.common_files))
print('----------------------------------------------------------')
print("common_funny:" + str(dirobj.common_funny))
print('----------------------------------------------------------')
print("same_file:" + str(dirobj.same_files))
print('----------------------------------------------------------')
print("diff_files:" + str(dirobj.diff_files))
print('----------------------------------------------------------')
print("funny_files:" + str(dirobj.funny_files))



















