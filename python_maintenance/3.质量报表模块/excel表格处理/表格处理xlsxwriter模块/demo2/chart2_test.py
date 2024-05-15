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
运行测试
"""
import os

FILE_PATH = os.path.join(os.path.dirname(__file__), '/demo2')


def simple_test():
    dimension_lst = ['all', 'isp']

    # 方式一：按文件拆分
    for dimension in dimension_lst:
        filename = os.path.join(FILE_PATH, f'竟对分析_SimpleTest_{dimension}.xlsx')
        sheetName, data = construct_test_data(dimension=dimension)
        export_simple_excel(filename=filename, sheetLst=[sheetName], contents=[data], dimensions=[dimension])
    # 方式二：按sheet拆分
    file = os.path.join(FILE_PATH, '竟对分析_SimpleTest.xlsx')
    sheetLst = []
    contents = []
    for dimension in dimension_lst:
        sheetName, data = construct_test_data(dimension=dimension)
        sheetLst.append(sheetName)
        contents.append(data)
    export_simple_excel(filename=file, sheetLst=sheetLst, contents=contents, dimensions=dimension_lst)


if __name__ == '__main__':
    simple_test()

