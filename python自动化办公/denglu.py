"""
title = ''
author = 'huifenghechang'
mtime = '2024/4/25'
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
Python实现注册登录功能
"""

import sqlite3
from tkinter import Tk, Label, Entry, Button, messagebox, W, E

#初始化数据库和用户表
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT PRIMARY KEY, password TEXT)''')
    conn.commit()
    conn.close()

init_db()

#注册用户的函数
def register_user():
    username = username_entry.get()
    password = password_entry.get()
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()
    messagebox.showinfo("成功", "用户注册成功！")
    root.destroy()

#登录用户的函数
def login_user():
    username = username_entry_login.get()
    password = password_entry_login.get()
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()
    conn.close()
    if user:
        messagebox.showinfo("成功", "登录成功！")
        root.destroy()
    else:
        messagebox.showerror("错误", "用户名或密码错误！")

#切换到登录界面
def switch_to_login():
    root.destroy()
    create_login_ui()

#切换到注册界面
def switch_to_register():
    root.destroy()
    create_register_ui()

#创建注册界面
def create_register_ui():
    global root, username_entry, password_entry
    root = Tk()
    root.title("用户注册")

    #用户名标签和输入框
    Label(root, text="用户名:").grid(row=0, column=0, sticky=W, padx=10, pady=10)
    username_entry = Entry(root)
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    #密码标签和输入框
    Label(root, text="密码:").grid(row=1, column=0, sticky=W, padx=10, pady=10)
    password_entry = Entry(root, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    #注册按钮
    Button(root, text="注册", command=register_user).grid(row=2, column=0, padx=10, pady=10)

    #切换到登录界面的按钮
    Button(root, text="已有账号？去登录", command=switch_to_login).grid(row=2, column=1, padx=10, pady=10)

    root.mainloop()

#创建登录界面
def create_login_ui():
    global root, username_entry_login, password_entry_login
    root = Tk()
    root.title("用户登录")

    #用户名标签和输入框
    Label(root, text="用户名:").grid(row=0, column=0, sticky=W, padx=10, pady=10)
    username_entry_login = Entry(root)
    username_entry_login.grid(row=0, column=1, padx=10, pady=10)

    #密码标签和输入框
    Label(root, text="密码:").grid(row=1, column=0, sticky=W, padx=10, pady=10)
    password_entry_login = Entry(root, show="*")
    password_entry_login.grid(row=1, column=1, padx=10, pady=10)

    #登录按钮
    Button(root, text="登录", command=login_user).grid(row=2, column=0, padx=10, pady=10)

    #切换到注册界面的按钮
    Button(root, text="还没有账号？去注册", command=switch_to_register).grid(row=2, column=1, padx=10, pady=10)

    root.mainloop()

#运行程序，初始显示注册界面
if __name__ == "__main__":
    create_register_ui()