# encoding=utf-8

import time

with open('tmp.txt', 'rb') as f:
    f.seek(0, 2)  # 将光标移动至文件末尾
    while True:  # 实时显示文件新增加的内容
        line = f.read()
        if line:
            print(line.decode('utf-8'), end='')
        else:
            time.sleep(0.2)  # 读取完毕后短暂的睡眠
