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
将数据库查询出来的数据录入xlsx文件
"""

import pymysql
from datetime import datetime
import xlsxwriter

# 创建mysql连接
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='abc123', db='zqs')
cursor = conn.cursor()

sql1 = "select empno,ename , mgr,hiredate from emp where 1 = 1"
headers = ["empno", "ename", "mgr", "hiredate"]

cursor.execute(sql1)

rows = cursor.fetchall()
fields = cursor.description  # 获取列名

# 创建一个workbook和worksheet
workbook = xlsxwriter.Workbook('emp01.xlsx')
worksheet = workbook.add_worksheet()

# 新增一个粗体格式
bold = workbook.add_format({'bold': True})

# 写表头
worksheet.write('A1', 'empno', bold)
worksheet.write('B1', 'ename', bold)
worksheet.write('C1', 'mgr', bold)
worksheet.write('D1', 'hiredate', bold)

# 数据坐标0,0 ~ row,col   row取决于：result的行数；col取决于fields的总数
for row in range(1, len(rows) + 1):
    for col in range(0, len(fields)):
        worksheet.write(row, col, u'%s' % rows[row - 1][col])
workbook.close()

# 关闭连接
cursor.close()
conn.close()
