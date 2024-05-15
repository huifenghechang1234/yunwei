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
绘制图表
"""
import xlsxwriter

color_lst = [
    ['#000000', '#312D30', '#444245'],  # 黑色
    ['#DDEBCF', '#9CB86E', '#156B13'],  # 绿色
    ['#0000FF', '#6A98CC', '#46A7F5'],  # 蓝色
    ['#800000', '#633915', '#A45D2D'],  # 棕色
    ['#00FFFF', '#29CFCD', '#006054'],  # 青色
    ['#808080', '#76797E', '#878785'],  # 灰色
    ['#FF0000', '#801801', '#D70F19'],  # 红色
    ['#C0C0C0', '#C2C2C2', '#8A8687'],  # 银色
    ['#800080', '#621C9B', '#46024F'],  # 紫色
    ['#FFFF00', '#F2BF04', '#FFE057'],  # 黄色
    ['#FFFFFF', '#FCFAFB', '#CECECC'],  # 白色
]


def export_simple_excel(filename=None, sheetLst=None, contents=None, dimensions=None):
    filename = filename if filename else '竟对_xlsxwriter_Test.xlsx'
    sheetLst = sheetLst if sheetLst else ['竟对分析测试']
    contents = contents if contents else []
    dimensions = dimensions if dimensions else ['all', 'isp']
    wb = xlsxwriter.Workbook(filename)

    # 设置风格
    style1 = wb.add_format({
        "bold": True,
        'font_name': '仿宋',
        'font_size': 12,
        'bg_color': '#4DCFF6',
        "align": 'center',
        "valign": 'vcenter',
        'text_wrap': 1
    })
    style2 = wb.add_format({
        'font_size': 11,
        'font_color': '#217346',
        'bg_color': '#E6EDEC',
        "align": 'center',
        "valign": 'vcenter',
    })

    for index_, sheetName in enumerate(sheetLst):
        ws = wb.add_worksheet(name=sheetName)
        dimension = dimensions[index_]
        # ws.set_default_row(35)  # 设置默认行高
        ws.set_column(0, len(contents[index_][0]) - 1, 20)  # 设置列宽
        # 写入
        if dimension == 'all':
            for i, row_lst in enumerate(contents[index_]):
                style = style2 if i != 0 else style1
                ws.write_row(f'A{i + 1}', row_lst, style)
        else:
            line1, line2 = list(filter(lambda col: col, contents[index_][0])), list(
                filter(lambda col: col, contents[index_][1]))
            isp, titleLine1 = line1[0], line1[1:]
            titleLine2 = line2
            ws.set_column(0, 0, 20)  # 设置列宽
            ws.set_column(1, len(titleLine2), 15)  # 设置列宽
            # 标题
            ws.merge_range(0, 0, 1, 0, isp, style1)
            [ws.merge_range(0, 2 * i + 1, 0, 2 * (i + 1), name, style1) for i, name in enumerate(titleLine1)]
            [ws.write(1, i + 1, name, style1) for i, name in enumerate(titleLine2)]
            # 内容
            for i, row_lst in enumerate(contents[index_][2:]):
                ws.write_row(f'A{i + 3}', row_lst, style2)

        # 画图
        y1_name = '延时（ms）'
        y2_name = '丢包率（%）'
        x_name = '产品类型'
        title_name = sheetName

        # 柱状图
        column_chart = wb.add_chart({'type': 'column'})
        # 折线图
        line_chart = wb.add_chart({'type': 'line'})

        if dimension == 'all':  # 整体维度
            column_name = f'={sheetName}!A2'
            line_name = f'={sheetName}!A3'
            categories = f'={sheetName}!B1:H1'
            column_values = f'={sheetName}!B2:H2'
            line_values = f'={sheetName}!B3:H3'

            column_chart.add_series({
                'name': column_name,
                'categories': categories,
                'values': column_values,
            })
            line_chart.add_series({
                'name': line_name,
                'categories': categories,
                'values': line_values,
                'marker': {'type': 'circle'},  # 系列标记
                'data_labels': {  # 数据标签
                    'value': True,
                    'series_name': True,
                    'position': 'above',
                    'separator': "\n",
                    'font': {'name': 'Consolas', 'color': 'red', 'size': 8}
                },
                'y2_axis': True,
            })
        else:  # 运营商维度
            # 添加规则
            d_lst = ['B', 'D', 'F', 'H', 'J', 'L', 'N']
            l_lst = ['C', 'E', 'G', 'I', 'K', 'M', 'O']

            for i, c in enumerate(d_lst):
                # 写法一
                categories_str = f'={sheetName}!A3:A5'
                column_name_str = f'={sheetName}!{c}1:{c}2'
                line_name_str = f'={sheetName}!{l_lst[i]}1:{l_lst[i]}2'
                column_values_str = f'={sheetName}!{c}3:{c}5'
                line_values_str = f'={sheetName}!{l_lst[i]}3:{l_lst[i]}5'

                # 添加数据选项
                column_chart.add_series({
                    'name': column_name_str,
                    'categories': categories_str,
                    'values': column_values_str,
                    'gap': 50,  # 间隙
                    'overlap': -5,  # 系列重叠
                    'gradient': {  # 渐变填充
                        'colors': color_lst[i],
                        'type': 'radial'
                    },
                })
                line_chart.add_series({
                    'name': line_name_str,
                    'categories': categories_str,
                    'values': line_values_str,
                    'marker': {'type': 'circle'},  # 系列标记
                    'data_labels': {  # 数据标签
                        'value': True,
                        'series_name': True,
                        'position': 'above',
                        'separator': "\n",
                        'font': {'name': 'Consolas', 'color': 'yellow', 'size': 8}
                    },
                    'y2_axis': True,
                })

        # 设置副坐标
        line_chart.set_y2_axis({
            'name': y2_name,
            'name_font': {'name': 'Calibri', 'color': 'red'},  # 轴标题设置
            'num_font': {'name': 'Arial', 'color': '#00B0F0', 'size': 8},  # 轴参数设置
        })
        # 设置前、背景色
        column_chart.set_plotarea({
            'pattern': {
                'pattern': 'percent_5',
                'fg_color': '#555555',
                'bg_color': '#595959',
            }
        })
        # 组合
        column_chart.combine(line_chart)
        column_chart.set_title({'name': title_name, 'name_font': {'name': 'Calibri', 'color': 'red', 'size': 15}})
        column_chart.set_x_axis({'name': x_name, 'name_font': {'name': 'Calibri', 'color': 'green'},
                                 'num_font': {'name': 'Arial', 'color': 'green', 'size': 9}})
        column_chart.set_y_axis({'name': y1_name, 'name_font': {'name': 'Calibri', 'color': 'blue'},
                                 'num_font': {'name': 'Arial', 'color': 'blue', 'size': 8}})
        # 样式
        column_chart.set_style(2)
        column_chart.set_legend({'font': {'size': 8, 'bold': False}})
        column_chart.set_size({'width': 720, 'height': 576})
        # 插入
        ws.insert_chart('A4', column_chart, {'x_offset': 25, 'y_offset': 10})  # 在A4单元格插入图表
    # 保存关闭文件
    wb.close()





