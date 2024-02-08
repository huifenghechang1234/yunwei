"""
title = ''
author = 'huifenghechang'
mtime = '2023/12/10'
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
xlsxwriter简介
新建 xlsx 文件，插入数据、插入图标等表格操作。只能新建xlsx后写入xlsx文件

写入
"""

import xlsxwriter
from datetime import datetime

# 创建工作簿
workbook = xlsxwriter.Workbook('测试文件.xlsx')  # 创建一个excel文件

# 创建工作表
worksheet = workbook.add_worksheet('这是sheet1')  # 在文件中创建一个名为这是sheet1的sheet,不加名字默认为sheet1

# 写入数据
worksheet.write(0, 0, '写点什么好')  # 写入字符串

worksheet.write(2, 0, '=SUM(B3:B4)')  # 写入excel公式
worksheet.write_formula(4, 0, '=SUM(B3:B4)')  # 写入excel公式

date_format = workbook.add_format({'num_format': 'yyyy-mm-dd H:M:S'})
date_format1 = workbook.add_format({'num_format': 'yyyy/m/d;@'})

worksheet.write_datetime(6, 0, datetime.today(), date_format)  # 写入自定义时间
worksheet.write_datetime(6, 2, datetime.today(), date_format1)  # 写入日期

num_format = workbook.add_format({'num_format': '0.00_);[Red](0.00)'})
worksheet.write_number(8, 0, 1001)  # 写入数字（常规）
worksheet.write_number(8, 2, 1001, num_format)  # 写入数字（数值）

worksheet.write_row(row=1, col=3, data=['嘿嘿', '哈哈', '呵呵'])  # 按行写入：从第几行开始，从第几列开始，写入的值

workbook.close()

