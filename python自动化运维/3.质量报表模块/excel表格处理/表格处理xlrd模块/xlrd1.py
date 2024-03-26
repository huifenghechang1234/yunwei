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
"""
xlrd读取excel的基础方法
1.打开文件对象：fb = xlrd.open_workbook(‘xls测试用例文件路径’)
2.获取工作表名称：sheetnames = fb.sheet_names()
3.打开测试用例所在工作表: casesheet = fb.get_by_name(‘’用例所在工作表名称)
4.获取测试用例条数（表格行数）：rows = casesheet.nrows
5.获取工作表内单元格值：cell_value = casesheet.cell_values(x, y)，其中x
和y为单元格的横坐标和纵坐标
6.由于需要通过pytest的装饰器进行参数化，所以读取到的单元格需要组合成列表的模板
"""

# 一、使用xlrd模块对xls文件进行读操作
# 一个Excel文件，就相当于一个“工作簿”(workbook)，一个“工作簿”里面可以包含多个“工作表（sheet）”
# 1获取工作簿对象
# 引入模块，获得工作簿对象。
import xlrd  # 引入模块

# 打开文件，获取excel文件的workbook（工作簿）对象
workbook = xlrd.open_workbook("DataSource/Economics.xls")  # 文件路径

# 2、获取工作表对象
# 当我们获取“工作簿对象”后，可以接着来获取工作表对象，可以通过“索引”的方式获得，也可以通过“表名”的方式获得
'''对workbook对象进行操作'''

# 获取所有sheet的名字
names = workbook.sheet_names()
print(names)  # ['各省市', '测试表']  输出所有的表名，以列表的形式

# 通过sheet索引获得sheet对象
worksheet = workbook.sheet_by_index(0)
print(worksheet)  # <xlrd.sheet.Sheet object at 0x000001B98D99CFD0>

# 通过sheet名获得sheet对象
worksheet = workbook.sheet_by_name("各省市")
print(worksheet)  # <xlrd.sheet.Sheet object at 0x000001B98D99CFD0>

# 由上可知，workbook.sheet_names() 返回一个list对象，可以对这个list对象进行操作
sheet0_name = workbook.sheet_names()[0]  # 通过sheet索引获取sheet名称
print(sheet0_name)  # 各省市

# 3、获取工作表的基本信息
# 在获得“表对象”之后，我们可以获取关于工作表的基本信息。包括表名、行数与列数
'''对sheet对象进行操作'''
name = worksheet.name  # 获取表的姓名
print(name)  # 各省市

nrows = worksheet.nrows  # 获取该表总行数
print(nrows)  # 32

ncols = worksheet.ncols  # 获取该表总列数
print(ncols)  # 13

# 4 按行或列方式获得工作表的数据
# 有了行数和列数，循环打印出表的全部内容也变得轻而易举
for i in range(nrows):  # 循环打印每一行
    print(worksheet.row_values(i))  # 以列表形式读出，列表中的每一项是str类型
# ['各省市', '工资性收入', '家庭经营纯收入', '财产性收入', ………………]
# ['北京市', '5047.4', '1957.1', '678.8', '592.2', '1879.0，…………]

col_data = worksheet.col_values(0)  # 获取第一列的内容
print(col_data)

# 5、获取某一个单元格的数据
# 我们还可以将查询精确地定位到某一个单元格。
# 在xlrd模块中，工作表的行和列都是从0开始计数的。
# 通过坐标读取表格中的数据
cell_value1 = sheet0.cell_value(0, 0)
cell_value2 = sheet0.cell_value(1, 0)
print(cell_value1)  # 各省市
print(cell_value2)  # 北京市

cell_value1 = sheet0.cell(0, 0).value
print(cell_value1)  # 各省市
cell_value1 = sheet0.row(0)[0].value
print(cell_value1)  # 各省市
