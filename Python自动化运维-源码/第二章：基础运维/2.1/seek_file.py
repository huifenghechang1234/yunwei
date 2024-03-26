# -*- coding: utf-8 -*-
# !/usr/local/bin/python
# Time: 2018/5/23 22:56:26
# Description:
# File Name: seek_file.py

f = open("tmp.txt", "rb+")
f.write(b"abcdefghi")
f.seek(5)  # 移动到文件的第六个字节
print(f.read(1))
f.seek(-3, 2)  # 移动到文件的倒数第三字节
print(f.read(1))

