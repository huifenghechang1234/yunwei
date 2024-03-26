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
本次实践通过定制网站5个频道的流量报表周报，通过XIsxWriter 模块将流量数据写人
Excel 文档，同时自动计算各频道周平均流量，再生成数据图表。具体是通过 workbook.add
chart(ftype: column)方法指定图表类型为柱形，使用write row、write column 方法分别以
行、列方式写入数据，使用add format0)方法定制表头、表体的显示风格，使用add series()
方法将数据添加到图表，同时使用chartset sizeset titleset y axis 设置图表的大小及标
题属性，最后通过 insert chart 方法将图表插入工作表中

操作步骤：
1 创建workbook对象及 worksheet 对象
workbook
workbook.add_worksheet
2准备相应的数据
add_column
add_row
3设定基本表现样式和字体样式
add_format()
format对象.add_xxx()
4 创建对应的图表
add_chart()
5为图表添加数据
add_series()
6修饰图表样式
add_title(),add_x_axis (),add_style()等
7 添加图表到工作表中
insert_chart()
8 关闭文件
close()


在Excel中，Sheet1!$B$1:$H$1 是一个绝对引用，它指向Sheet1工作表中从B1到H1的单元格范围。
这里的$符号表示绝对引用，意味着无论公式如何复制或移动，它始终会引用Sheet1工作表中的B1到H1这些特定的单元格。

通常，在Excel公式中，单元格引用可以是相对的、绝对的或混合的。相对引用（没有$符号）会根据公式所在单元格的位置而改变；
绝对引用（有$符号）则始终保持不变；混合引用则有一个或两个维度是相对引用，另一个维度是绝对引用。

在Sheet1!$B$1:$H$1中：
Sheet1! 表示这个引用指向名为Sheet1的工作表。
$B$1 表示绝对引用B1单元格。
:$H$1 表示从B1到H1的范围，且都是绝对引用。

因此，如果你在一个公式中使用Sheet1!$B$1:$H$1，它将始终引用Sheet1工作表中的第一行的B列到H列的单元格，
不受公式复制或移动的影响。这在创建图表的数据系列时特别有用，因为你需要确保引用的范围保持不变，以便图表能够正
确地引用数据
"""

import xlsxwriter

# 1.创建xlsx文件和工作表、图样式
workbook1 = xlsxwriter.Workbook('chart.xlsx')  # 创建一个Excel文件
worksheet = workbook1.add_worksheet()  # 创建一个工作表对象
chart1 = workbook1.add_chart({'type': 'column'})  # 创建一个图表对象

# 2.准备数据
# 2.1 标题数据
# 定义数据表头列表
title = [u'业务名称', u'星期一', u'星期二', u'星期三', u'星期四', u'星期五', u'星期六', u'星期日', u'平均流量']
# 2.2 频道数据
buname = [u'业务官网', u'新闻中心', u'购物频道', u'体育频道', u'亲子频道']  # 定义频道名称

# 2.3 流量数据
# 定义5频道一周7天流量数据列表
data = [
    [150, 152, 158, 149, 155, 145, 148],
    [89, 88, 95, 93, 98, 100, 99],
    [201, 200, 198, 175, 170, 198, 195],
    [75, 77, 78, 78, 74, 70, 79],
    [88, 85, 87, 90, 93, 88, 84],
]

# 3.定制样式
# 3.1通用数据格式
format = workbook1.add_format()  # 定义format格式对象
format.set_border(1)  # 定义 format对象单元格边框加粗(1像素的格式


# 3.2标题格式
format_title = workbook1.add_format()  # 定义 format title格式对象
format_title.set_border(1)  # 定义format title对象单元格边框加粗 (1像素)的格式
format_title.set_bg_color('#cccccc')  # 定义 format title 对象单元格背景颜色为cccccc’的格式
format_title.set_align('center')  # 定义 format title对象单元格居中对齐的格式
format_title.set_bold()  # 定义 format title对象单元格内容加租的格式


# 3.3统计数据格式
# 定义 formatave格式对象
format_ave = workbook1.add_format()
# 定义 formatave 对象单元格边框加粗(1像素)的格式
format_ave.set_border(1)
format_ave.set_num_format('0.00')  # 定义format ave 对象单元格数字类别显示格式

# 4.数据添加
# 4.1 数据添加
# 下面分别以行或列写入方式将标题、业务名称、流量数据写入起初单元格，同时引用不同格式对象
# 这行代码将title列表或数组中的数据写入工作表的A1行开始的单元格中。数据将按列表中的顺序从左到右填充单元格。format_title是用于设置这些单元格格式的格式对象
worksheet.write_row('A1', title, format_title)  # 标题是横向输入

# 这行代码将buname列表或数组中的数据写入工作表的A2列开始的单元格中。数据将按列表中的顺序从上到下填充单元格。format是用于设置这些单元格格式的格式对象
worksheet.write_column('A2', buname, format)  # 频道是纵向输入

# 统计的数据是横向输入
# 这行代码将data[0]列表或数组中的数据写入工作表的B2行开始的单元格中。data[0]是data列表的第一个元素，它应该也是一个列表或数组。format是用于设置这些单元格格式的格式对象
worksheet.write_row('B2', data[0], format)

worksheet.write_row('B3', data[1], format)
worksheet.write_row('B4', data[2], format)
worksheet.write_row('B5', data[3], format)
worksheet.write_row('B6 ', data[4], format)

# 4.2 统计数据添加
# 定义图表数据系列函数
def chart1_series(cur_row):
    worksheet.write_formula('I' + cur_row, \
                            '=AVERAGE(B' + cur_row + ':H' + cur_row + ')', format_ave)  # 计算(AVERAGE函数)频道周平均流量
    # 这行代码在Excel的当前工作表中的第cur_row行的I列写入一个公式，用于计算从B列到H列的平均值，并将结果格式化为format_ave
    # 'I' + cur_row：这部分代码将字符串'I'与变量cur_row（表示行号）拼接起来，生成一个类似于'I1'、'I2'等的字符串，它代表了Excel工作表中某个单元格的地址

    # 在Excel中，Sheet1!$B$1:$H$1 是一个绝对引用，它指向Sheet1工作表中从B1到H1的单元格范围
    chart1.add_series({
        'categories': '=Sheet1!$B$1:$H$1',
        # 将“星期一至星期日”作为图表数据标签 (X 轴),这定义了图表的X轴标签，即“星期一至星期日”。这里假设这些标签位于Sheet1的工作表的第一行的B列到H列

        'values': '=Sheet1!$B$' + cur_row + ':$H$' + cur_row,
        # 频道一周所有数据作为数据区城  这定义了图表的数据区域。它取Sheet1的工作表中从B列到H列、从第1行到cur_row行的数据。这意味着它正在取当前行及其之前的所有数据

        'line': {'color': 'black'},  # 线条颜色定义为 black(黑色)
        'name': '=Sheet1!$A$' + cur_row,  # 引用业务名称为图例项 这定义了图例项的名称。它从Sheet1的工作表的第cur_row行的A列取得。换句话说，它引用业务名称为图例项
    })

# 这段for循环的目的是为Excel工作表中的第2行到第6行的每一行数据创建一个图表数据系列。每次循环迭代都会调用chart1_series函数，并为相应的行号创建一个新的图表数据系列
# 对于每个整数row，它调用chart1_series函数，并将row的字符串形式作为参数传递
for row in range(2, 7):  # 数据域以第2~6行进行图表数据系列函数调用
    chart1_series(str(row))  # 在循环的每次迭代中，chart1_series函数被调用，并且row的当前值被转换为字符串（使用str(row)）后作为参数传递。这是必要的，因为chart1_series函数期望接收一个字符串，该字符串表示Excel工作表中的行号

for row in range(2, 7):  # 数据域以第2~6行进行图表数据系列函数调用
    chart1_series(str(row))

# 5图样式修改
# chart1.set_table()  # 设置X 轴表格格式，本示例不启用
# chart1.set_style(2)  # 设置图表样式，本示例不启用

# 5.1 图大小定制
chart1.set_size({'width': 577, 'height': 287})  # 设置图表大小
# 5.2 图标题定制
chart1.set_title({'name': u'业务流量周报图表'})  # 设置图表(上方)大标题
# 5.3 图的xy坐标定制
chart1.set_y_axis({'name': 'Mb/s', "name_font": {"size": 16}})  # 设置 y轴(左侧)小标题
chart1.set_x_axis({'name': '天数', "name_font": {"size": 14}})  # 设置 y轴(左侧)小标题
# 5.4 图的嵌入
worksheet.insert_chart('A8', chart1)  # 在A8单元格插入图表

# 饼图的绘制
chart2 = workbook1.add_chart({'type': 'pie'})  # 创建一个图表对象
def chart2_series(cur_row):
    # 在Excel中，Sheet1!$B$1:$H$1 是一个绝对引用，它指向Sheet1工作表中从B1到H1的单元格范围
    chart2.add_series({
        'categories': '=Sheet1!$B$1:$H$1',
        # 将“星期一至星期日”作为图表数据标签 (X 轴),这定义了图表的X轴标签，即“星期一至星期日”。这里假设这些标签位于Sheet1的工作表的第一行的B列到H列

        'values': '=Sheet1!$B$' + cur_row + ':$H$' + cur_row,
        # 频道一周所有数据作为数据区城  这定义了图表的数据区域。它取Sheet1的工作表中从B列到H列、从第1行到cur_row行的数据。这意味着它正在取当前行及其之前的所有数据

        'line': {'color': 'black'},  # 线条颜色定义为 black(黑色)
        'name': '=Sheet1!$A$' + cur_row,  # 引用业务名称为图例项 这定义了图例项的名称。它从Sheet1的工作表的第cur_row行的A列取得。换句话说，它引用业务名称为图例项
    })
for row in range(2, 7):  # 数据域以第2~6行进行图表数据系列函数调用
    chart2_series(str(row))  # 在循环的每次迭代中，chart1_series函数被调用，并且row的当前值被转换为字符串（使用str(row)）后作为参数传递。这是必要的，因为chart1_series函数期望接收一个字符串，该字符串表示Excel工作表中的行号

for row in range(2, 7):  # 数据域以第2~6行进行图表数据系列函数调用
    chart2_series(str(row))

# 5.1 图大小定制
chart2.set_size({'width': 577, 'height': 287})  # 设置图表大小
# 5.2 图标题定制
chart2.set_title({'name': u'业务流量周报图表'})  # 设置图表(上方)大标题
# 5.4 图的嵌入
worksheet.insert_chart('K8', chart2)  # 在A8单元格插入图表


# 6.关闭文件
workbook1.close()  # 关闭 Excel文档
