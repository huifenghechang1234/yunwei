# encoding=utf-8

import os
import datetime

# 循环e:\job目录和子目录 r表示原始字符串，不含转义字符
print(f"当前时间：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
for root, dirs, files in os.walk(r"e:\job"):
    for file in files:
        # 获取文件的绝对路径
        absPathFile = os.path.join(root, file)
        # 获取修改时间并转化为datetime类型
        modifiedTime = datetime.datetime.fromtimestamp(os.path.getmtime(absPathFile))
        now = datetime.datetime.now()  # 获取当前时间
        diffTime = now - modifiedTime  # 获取时间差
        # 打印相关信息，ljust(25)表示该字符串若不足25字节则右补空格
        # diffTime.days指间隔的天数，diffTime.seconds表示间隔除了天数外还剩余的秒数，将其转化为时和分
        # diffTime.seconds//3600： 对3600秒取整表示小时数
        # (diffTime.seconds%3600)//60：先对3600秒取余，再对60秒取整，表示分钟数
        # print(f"{absPathFile}".ljust(25), f"修改时间[{modifiedTime.strftime('%Y-%m-%d %H:%M:%S')}] \
        # 距今[{diffTime.days}天{diffTime.seconds//3600}时{(diffTime.seconds%3600)//60}分]")
        print(
            f"{absPathFile:<27s}修改时间[{modifiedTime.strftime('%Y-%m-%d %H:%M:%S')}] 距今[{diffTime.days:3d}天{diffTime.seconds//3600:2d}时{(diffTime.seconds%3600)//60:2d}分]"
        )
