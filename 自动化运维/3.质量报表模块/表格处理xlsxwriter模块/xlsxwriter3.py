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
列宽和行高
"""

import xlsxwriter

# 创建工作簿
workbook = xlsxwriter.Workbook('测试文件.xlsx')

# 创建工作表
worksheet = workbook.add_worksheet('这是sheet1')

# 写入数据
worksheet.write(0, 0, '这是个很长的字段')
worksheet.write(2, 2, '这是个特别长的字段')

# 设置行宽
worksheet.set_row(0, 60)    # 第一行行宽

# 设置列宽
worksheet.set_column(1, 2, 30)   # 第二、三列列宽

workbook.close()
