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
合并单元格
语法：
merge_range(first_row, first_col, last_row, last_col, data[, cell_format])
"""

import xlsxwriter
from datetime import datetime

# 创建工作簿
workbook = xlsxwriter.Workbook('测试文件.xlsx')

# 创建工作表
worksheet = workbook.add_worksheet('这是sheet1')

# 写入数据
worksheet.write(0, 0, '未合并') # 第一行第一列，A1写入'未合并'
worksheet.write(2, 0, '会被覆盖') # 第三行第一列，A3写入'会被覆盖'
worksheet.write(4, 0, '待合并') # 第五行第一列，A5写入'待合并'
worksheet.merge_range(1,2,3,4,'合并01') # 合并第二行-四行，第三列-五列，即：C2:E4
worksheet.merge_range('A3:B3','覆盖它') # 合并A3:B3，并写入'覆盖它'
worksheet.merge_range('A5:B5','') # 合并A5:B5，'待合并'并不被覆盖

workbook.close()
