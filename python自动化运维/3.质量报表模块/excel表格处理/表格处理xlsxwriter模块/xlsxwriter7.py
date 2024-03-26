"""
title = ''
author = 'huifenghechang'
mtime = '2024/2/23'
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
将指定格式的数据录入xlsx文件
增加列头
将金额加上$ 符号
"""

import xlsxwriter

# 创建一个workbook,新增一个worksheet
workbook = xlsxwriter.Workbook('Expenses02.xlsx')
worksheet = workbook.add_worksheet()

# 新增一个粗体格式
bold = workbook.add_format({'bold': True})

# 新增一个数值格式代表金额
money = workbook.add_format({'num_format': '$#,##0'})

# 写入表头
worksheet.write('A1', 'Item', bold)
worksheet.write('B1', 'Cost', bold)

# 以下的元组嵌套列表数据需要写入上面创建的worksheet
expenses = (
    ['Rent', 1000],
    ['Gas', 100],
    ['Food', 300],
    ['Gym', 50],
)

# 定义起始行和列为0
row = 1
col = 0

# 遍历数据并逐行写入xlsx文件
for item, cost in (expenses):
    worksheet.write(row, col, item)
    worksheet.write(row, col + 1, cost, money)
    row += 1

# 写一个公式汇总数据
worksheet.write(row, 0, 'Total', bold)
worksheet.write(row, 1, '=sum(B2:B5)', money)

# 关闭workbook
workbook.close()
