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
功能描述：
从数据库取数，写入xlsx，并发送邮件
"""

# util为博主封装的模块
from util import config
from util.gmail import Mail
from util.gstring import convert_df_to_html
from util.logger import log
from util.db import get_db
import pandas as pd
import os
from datetime import datetime
import xlsxwriter


def run(init_date):
    # 创建excel文件
    new_excel = "6（1）班考试成绩单-" + init_date + ".xlsx"  # 附件
    if os.path.exists(new_excel):
        os.remove(new_excel)
    workbook = xlsxwriter.Workbook(new_excel)

    # 数据库连接
    db = get_db("dbcenter")

    # 数据库取数
    log.info('开始从数据库取数...')
    math_sql = f'''
        select '张三' as name
               ,'6（1）班' as class
               ,'数学' as subject
               ,95 as score
               ,{init_date} as init_date
        union all
        select '李四' as name
               ,'6（1）班' as class
               ,'数学' as subject
               ,98 as score
               ,{init_date} as init_date
        union all
        select '王五' as name
               ,'6（1）班' as class
               ,'数学' as subject
               ,null as score
               ,{init_date} as init_date
        '''

    chinese_sql = f'''
        select '张三' as name
               ,'6（1）班' as class
               ,'语文' as subject
               ,90 as score
               ,{init_date} as init_date
        union all
        select '李四' as name
               ,'6（1）班' as class
               ,'语文' as subject
               ,88 as score
               ,{init_date} as init_date
        union all
        select '王五' as name
               ,'6（1）班' as class
               ,'语文' as subject
               ,70 as score
               ,{init_date} as init_date
        '''

    sqls = [math_sql, chinese_sql]
    sheets = ['数学成绩单', '语文成绩单']
    title_format = {
        'font_name': '宋',  # 字体
        'font_size': 10,  # 字体大小
        'font_color': 'black',  # 字体颜色
        'bold': True,  # 是否粗体
        'align': 'center',  # 水平居中对齐
        'valign': 'vcenter'  # 垂直居中对齐
    }
    format = {
        'font_name': '宋',  # 字体
        'font_size': 10,  # 字体大小
        'font_color': 'black',  # 字体颜色
        'bold': False,  # 是否粗体
        'align': 'center',  # 水平居中对齐
        'valign': 'vcenter'  # 垂直居中对齐
    }
    date_format = {
        'font_name': '宋',  # 字体
        'font_size': 10,  # 字体大小
        'font_color': 'black',  # 字体颜色
        'align': 'center',  # 水平居中对齐
        'valign': 'vcenter',  # 垂直居中对齐
        'num_format': 'yyyy/mm/dd'
    }
    title_style = workbook.add_format(title_format)
    style = workbook.add_format(format)
    date_style = workbook.add_format(date_format)
    for i in range(0, len(sqls)):
        datas = db.query(sqls[i], {init_date: init_date})
        df = pd.DataFrame(datas, columns=['name', 'class', 'subject', 'score', 'init_date'])
        df["班主任"] = '王老师'
        df["考试日期"] = datetime.strptime(init_date, '%Y%m%d').date()
        df = df.rename(columns={"name": "姓名", "class": "班级", "subject": "科目", "score": "分数"})
        order = ["考试日期", "班级", "班主任", "姓名", "科目", "分数"]
        df = df[order].fillna(0)  # 缺考分数为0
        log.info(df)
        datas = [tuple(xi) for xi in df.values]
        excel_data = [tuple(order)] + datas
        worksheet = workbook.add_worksheet(sheets[i])
        for i in range(0, len(excel_data)):
            for j in range(0, len(excel_data[i])):
                if i == 0:
                    worksheet.write(i, j, excel_data[i][j], title_style)
                elif j == 0:
                    worksheet.write_datetime(i, j, datetime.strptime(init_date, '%Y%m%d').date(), date_style)  # 写入时间
                else:
                    worksheet.write(i, j, excel_data[i][j], style)
    workbook.close()

    # 发邮件
    # html = convert_df_to_html(df)
    mail_config = config.get_config("email.send_fxm")  # 发件人
    mail = Mail(mail_config)
    title = '6（1）班考试成绩单-' + init_date  # 邮件标题
    to_list = 'xxx.com'  # 收件人
    mail.send_email(to_list, title, content_text='各位家长你们好，6（1）班' + init_date + '日考试成绩单详见附件！',
                    attachment_list=[new_excel])


if __name__ == "__main__":
    init_date = '20220412'
    run(init_date)
