# -*- coding: utf-8 -*-
# !/usr/local/bin/python
# Time: 2018/5/23 20:55:29
# Description:
# File Name: lx_while.py

flag = True
while flag:
    input_str = input("please input something,'q' for quit.-> ")
    print("your input is %s" % input_str)
    if input_str == "q":
        flag = False
print("You're out of circulation.")
