"""
title = ''
author = 'huifenghechang'
mtime = '2024/1/24'
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
自动化办公  
树结构与深度优先搜索算法
目录搜索

path代表待搜索的目录路径
result存储搜索到的文件路径列表
"""

import os
import shutil  # shutil模块 实现移动文件的功能需要


# 函数将path目录中的全部子目录和文件找到报错到result
def search_dir(path, result):
    child_files = os.listdir(path)  # 使用os模块中的listdir得到path下的目录和文件，保存到child_files
    for child in child_files:  # 遍历child_files

        child = os.path.join(path, child)  # 通过join函数拼接子目录或文件；就，保存到child

        result.append(child)  # 将child结果保存到result

        if os.path.isdir(child):  # 如果child是一个子目录
            search_dir(child, result)  # 调用search_dir继续递归搜索child


# 输入搜索目录和doc文件保存的目录
input_dir = input("输入待搜索的目录:")
output_dir = input("输入保存文件的目录")

# 设置保存子目录与文件路径的列表files
files = list()  # 定义一个空列表

# 将input_dir中的全部子目录和文件
search_dir(input_dir, files)

for file in files:  # 遍历files
    print("find %s" % (file))  # 打印搜索到的路径

    # 如果该路径是一个docx文件
    if os.path.isfile(file) and file.endswitch('.docx'):
        print("move %s" % (file))  # 打印提示信息

        shutil.move(file, output_dir)  # 将文件移动到output_dir
