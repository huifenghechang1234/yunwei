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
写入数字
"""

import xlsxwriter
from datetime import datetime

# 创建工作簿
workbook = xlsxwriter.Workbook('测试文件6.xlsx')  # 创建一个excel文件

# 创建工作表
worksheet = workbook.add_worksheet('这是sheet1')  # 在文件中创建一个名为这是sheet1的sheet,不加名字默认为sheet1

# 写入数据
num_format = workbook.add_format({'num_format': '￥#,##0.00;￥-#,##0.00'})
worksheet.write(8, 0, 120,num_format)  # 写入数字（常规）

workbook.close()
