# -*- coding: utf-8 -*-
def score(num):  # 定义一个函数，判断得分属于哪个分类
    if num >= 90:
        print(num, "excellent")
    elif num >= 80:
        print(num, "fine")
    elif num >= 60:
        print(num, "pass")
    else:
        print(num, "bad")


score(99)  # 调用函数，下同
score(80)
score(70)
score(60)
score(59)

a = 3
b = 4
c = a if a < b else b
print(c)

flag = True
while flag:
    input_str = input("please input something,'q' for quit. ->")
    print("your input is %s" % input_str)
    if input_str == "q":
        flag = False
print("You're out of circulation.")


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


import re


# 菲波那切数列
def Fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return "亲！没有数据了..."


# 调用方法，生成出10个数来
f = Fib(10)
# 使用一个循环捕获最后return 返回的值，保存在异常StopIteration的value中
while True:
    try:
        x = next(f)
        print("f:", x)
    except StopIteration as e:
        print("生成器最后的返回值是：", e.value)
        break
