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
构造数据
"""

def construct_test_data(dimension='all'):
    """
    构造数据
    """
    if dimension == 'all':
    	sheetName = '国内_整体'
        data = [
            ['指标', '加速线路', '安全加速', '精品EIP', '普通EIP', '腾讯', 'AWS', '阿里云'],
            ['延时（ms）', 51.22, 56.12, 65.61, 92.76, 116.02, 76.02, 66.02],
            ['丢包率（%）', 1.45, 3.21, 0.74, 6.18, 2.32, 1.32, 0.62]
        ]
    else:
    	sheetName = '国内_运营商'
        data = [
            ['运营商', '加速线路', None, '安全加速', None, '精品EIP', None, '普通EIP', None, '腾讯', None, 'AWS', None, '阿里云', None],
            [None, '延时（ms）', '丢包率（%）', '延时（ms）', '丢包率（%）', '延时（ms）', '丢包率（%）', '延时（ms）', '丢包率（%）', '延时（ms）', '丢包率（%）', '延时（ms）', '丢包率（%）', '延时（ms）', '丢包率（%）'],
            ['中国电信', 52.68, 2, 42.1, 0.82, 24.21, 1.08, 52.32, 0.12, 50.97, 2, 121.2, 6.8, 90.33, 0.54],
            ['中国移动', 53.92, 0.3, 56.12, 2, 34, 0.27, 68.21, 1.45, 89.21, 0.42, 77.8, 0.52, 44.3, 0],
            ['中国联通', 67.31, 0.69, 65.15, 0.38, 88, 0.52, 55.52, 0.66, 80.2, 0.22, 92.3, 0.44, 210.2, 2.21]
        ]
    return sheetName, data

