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

操作步骤：
1.创建工作簿
2.创建工作表
3.设定基础格式
4.写入数据
5.退出操作

set_row(行位置，行号，单元格格式，其他属性)
see_column(列起始位置，列结束位置，列宽，单元格格式，其他属性)
insert_image(行位置，列位置，图片名称路径)

'yyyy-mm-dd H:M:S'是一个字符串，定义了日期时间的显示格式。具体来说：
yyyy：4位数的年份（例如：2023）
mm：2位数的月份（例如：09代表9月）
dd：2位数的日期（例如：17代表17日）
H：24小时制的小时数（例如：13代表下午1点）
M：分钟数（例如：45代表45分）
S：秒数（例如：30代表30秒）

'yyyy/m/d'：如果单元格的内容是一个日期值，则将其格式化为年/月/日的形式。例如，日期2023年9月17日将被显示为2023/09/17。
';@'：分号后面的部分是一个备用格式，用于当单元格的内容不是日期值时。@表示显示单元格内容的原始文本形式，不进行任何特殊的格式化。
这意味着如果单元格包含一个非日期值，它将按照其原始文本形式显示

这个格式字符串'0.00_);[Red](0.00)'的含义如下：
'0.00_'：当单元格的值为正数或零时，它将以两位小数的形式显示。下划线_通常用于表示数字的分隔符，但在这种情况下，
它可能是多余的，因为0.00已经明确指定了两位小数的格式。

);：分号表示格式字符串中的两部分之间的分隔。前半部分应用于正数和零，而后半部分应用于负数。

[Red](0.00)：当单元格的值为负数时，它将以红色显示，并且以两位小数的形式。方括号[ ]用于指定颜色的应用，
而(0.00)定义了负数的显示格式。
这个条件格式将使得正数和零以默认的颜色（通常是黑色）和两位小数的形式显示，而负数将以红色显示，并且也保留两位小数
"""

import xlsxwriter
from datetime import datetime

# 创建工作簿
workbook = xlsxwriter.Workbook('测试文件1.xlsx')  # 创建一个excel文件

# 创建工作表
worksheet = workbook.add_worksheet('这是sheet1')  # 在文件中创建一个名为这是sheet1的sheet,不加名字默认为sheet1
worksheet1 = workbook.add_worksheet('这是sheet2')

# 设定基础格式
# 列宽度
worksheet.set_column('A:A', 20)

# 字体格式
# bold = workbook.add_format({"bold": True})  # 字体加粗

my_format = workbook.add_format()
# 通用属性设置
my_format.set_bold()  # 字体加粗
my_format.set_color('blue')  # 设定字体颜色
my_format.set_font_size(10)  # 设定字体大小为10号

# 定制属性设置
# 方法1
my_bold = my_format.set_bold()  # 字体加粗
my_color = my_format.set_color('red')  # 设定字体颜色
my_size = my_format.set_font_size(16)  # 设定字体大小为16号

# 方法2
# my_bold = workbook.add_format({"bold": "true"})  # 字体加粗
# my_color = workbook.add_format({"color": "green"})  # 设定字体颜色
# my_size = workbook.add_format({"font_size": "10"})  # 设定字体大小为16号

# 增加图
workbook.add_chart({"type": "line"})  # 折线图
workbook.add_chart({"type": "radar"})  # 雷达图
workbook.add_chart({"type": "area"})  # 面积图

# 写入数据
worksheet.write(0, 0, '写点什么好')  # 写入字符串

worksheet.write(2, 0, '=SUM(B3:B4)')  # 写入excel公式
worksheet.write_formula(4, 0, '=SUM(B3:B4)')  # 写入excel公式

date_format = workbook.add_format({
    'num_format': 'yyyy-mm-dd H:M:S'})  # 这行代码是在使用某个Python库（很可能是openpyxl或xlwt，这两个库常用于处理Excel文件）来为一个Excel工作簿（workbook）添加一个自定义的格
date_format1 = workbook.add_format(
    {'num_format': 'yyyy/m/d;@'})  # 这行代码创建了一个新的格式对象date_format1，该对象被设置为在Excel中显示日期的一种特定格式

worksheet.write_datetime(6, 0, datetime.today(),
                         date_format)  # 写入自定义时间  这行代码将当前日期和时间写入工作表的第6行第0列，并使用date_format中定义的格式来显示这个日期和时间
worksheet.write_datetime(6, 2, datetime.today(), date_format1)  # 写入日期

num_format = workbook.add_format({'num_format': '0.00_);[Red](0.00)'})  # 这行代码创建了一个新的格式对象num_format，该对象定义了一个条件格式

# write_number()写人数字类型数据
worksheet.write_number(8, 0, 1001, my_color)  # 写入数字（常规）
worksheet.write_number(8, 2, 1001, num_format)  # 写入数字（数值）

worksheet.write_row(row=1, col=3, cell_format=my_format, data=['嘿嘿', '哈哈', '呵呵'])  # 按行写入：从第几行开始，从第几列开始，写入的值

# write_boolean()写人逻辑类型数据
worksheet.write_boolean(0, 0, True)

# write_url()写入超链接类型数据
worksheet.write_url('A5', 'ftp://www.python.org/')

# 添加图片数据
# 本地图片导入
worksheet.insert_image('C5', '1.png')

# 网络图片导入
worksheet.insert_image('F5', 'python.png', {"url": "https://www.python.org/"})

# 退出操作
workbook.close()
