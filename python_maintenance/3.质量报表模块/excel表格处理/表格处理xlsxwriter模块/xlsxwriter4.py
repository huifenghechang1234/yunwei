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
设置单元格样式
"""
import xlsxwriter

workbook = xlsxwriter.Workbook('测试文件4.xlsx')
worksheet = workbook.add_worksheet('这是sheet1')
title_format = {
    'font_name': '微软雅黑',  # 字体
    'font_size': 12,  # 字体大小
    'font_color': 'black',  # 字体颜色
    'bold': True,  # 是否粗体
    'bg_color': '#101010',  # 表格背景颜色
    'fg_color': '#00FF00',  # 前景颜色
    'align': 'center',  # 水平居中对齐
    'valign': 'vcenter',  # 垂直居中对齐
    # 'num_format': 'yyyy-mm-dd H:M:S',# 设置日期格式
    # 后面参数是线条宽度
    'border': 1,  # 边框宽度
    'top': 1,  # 上边框
    'left': 1,  # 左边框
    'right': 1,  # 右边框
    'bottom': 1  # 底边框
}
format = {
    'font_size': 10,  # 字体大小
    'font_color': 'blue',  # 字体颜色
    'bold': False,  # 是否粗体
    'bg_color': '#101010',  # 表格背景颜色
    'fg_color': '#00FF00',  # 前景颜色
    'align': 'center',  # 水平居中对齐
    'valign': 'vcenter',  # 垂直居中对齐
    # 'num_format': 'yyyy-mm-dd H:M:S',# 设置日期格式
    # 后面参数是线条宽度
    'border': 1,  # 边框宽度
    'top': 1,  # 上边框
    'left': 1,  # 左边框
    'right': 1,  # 右边框
    'bottom': 1  # 底边框
}
title_style = workbook.add_format(title_format)  # 设置样式format是一个字典
style = workbook.add_format(format)  # 设置样式format是一个字典
worksheet.write_row(0, 0, ['表头1', '表头2'], title_style)  # 第一行第一列开始写入表头
worksheet.write_row(1, 0, ['数据1', '数据2'], style)  # 第二行第一列开始写入数据
workbook.close()
