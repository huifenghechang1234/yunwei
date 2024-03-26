# -*- coding: utf-8 -*-
# 本文件应该保存为utf-8编码，否则会报错

str = "我是中国人"
print(f'Unicode字符串为"{str}"')
byte0 = str.encode("utf-8")
print(f'Unicode字符串"{str}"以utf-8编码得到字节串[{byte0}]')
str0 = byte0.decode("utf-8")
print(f'将utf-8字节串[{byte0}]解码得到Unicode字符串"{str0}"')
byte1 = str.encode("gbk")
print(f'Unicode字符串"{str}"以gbk编码得到字节串[{byte1}]')
str1 = byte1.decode("gbk")
print(f'将gbk字节串[{byte1}]解码得到Unicode字符串"{str1}"')

print(f'以文本方式将Unicode字符串"{str}"写入a.txt')

with open("a.txt", "w", encoding="gbk") as f:
    f.write(str)

print("以文本方式读取 a.txt 的内容")
with open("a.txt", "r", encoding="gbk") as f:
    print(f.read())
