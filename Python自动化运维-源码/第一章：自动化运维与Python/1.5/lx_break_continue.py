# -*- coding: utf-8 -*-
# !/usr/local/bin/python
# Time: 2018/5/23 20:57:36
# Description:
# File Name: lx_break_continue.py

print("break--------------")
count = 0
while count < 5:
    print("aaa", count)
    count += 1
    if count == 2:
        break
    print("bbb", count)

print("continue--------------")
count = 0
while count < 5:
    print("aaa", count)
    count += 1
    if count == 2:
        continue
    print("bbb", count)
