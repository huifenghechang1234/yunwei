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
workbook = xlsxwriter.Workbook('测试文件3.xlsx')

# 创建工作表
worksheet = workbook.add_worksheet('这是sheet1')

# 写入数据
worksheet.write(0, 0, '这是个很长的字段')
worksheet.write(2, 2, '这是个特别长的字段')

# 设置行宽
worksheet.set_row(0, 60)  # 第一行行宽
worksheet.write('A1', 'Hello')  # 在A1 单元格写入Hello 字符串
cell_format = workbook.add_format({'color': 'blue'})  # 定义一个蓝色的格式对象
worksheet.set_row(0, 40, cell_format)  # 设第1行单元格高度为40像素，且引用蓝色                                                   #格式对象
worksheet.set_row(1, None, None, {'hidden': 1})  # 隐藏第2行单元格

# 设置列宽
worksheet.set_column(1, 2, 30)  # 第二、三列列宽

worksheet.write('C3', 'Hello')  # 在A1单元格写入Hello 字符串
worksheet.write('D3', 'World')  # 在B1单元格写入World字符串
cell_format2 = workbook.add_format({'bold': True})  # 定义一个加粗的格式对象
worksheet.set_column(0, 1, 20, cell_format2)  # 设置0到1即(A到B)列单元格宽度为20像素，且引用加粗格式对象
worksheet.set_column('C:D', 20)  # 设置C到D列单元格宽度为20像素
worksheet.set_column('E:G', None, None, {'hidden': 1})  # 隐藏E到G列单元格

workbook.close()
