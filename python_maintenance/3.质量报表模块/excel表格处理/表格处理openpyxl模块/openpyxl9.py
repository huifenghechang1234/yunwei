"""
title = ''
author = 'huifenghechang'
mtime = '2024/2/24'
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
# 五、修改已经存在的工作簿(表)
# 1、插入一列数据
# 将第四节中最后保存的myfile.xlsx作为我们要修改的表格，我们计划在最前面插入一列“编号”，如下所示：
import openpyxl

workbook = openpyxl.load_workbook("myfile.xlsx")
worksheet = workbook.worksheets[0]

# 在第一列之前插入一列
worksheet.insert_cols(1)  #

for index, row in enumerate(worksheet.rows):
    if index == 0:
        row[0].value = "编号"  # 每一行的一个row[0]就是第一列
    else:
        row[0].value = index
# 枚举出来是tuple类型，从0开始计数

workbook.save(filename="myfile.xlsx")

# 2、修改特定单元格
worksheet.cell(2, 3, '0')
worksheet["B2"] = "Peking"

# 3、批量修改数据
# 批量修改数据就相当于写入，会自动覆盖。在上一节中已经有介绍，不再赘述。
# 还有sheet.append()
# 方法，可以用来添加行
taiwan = [32, "台湾省"]
worksheet.append(taiwan)