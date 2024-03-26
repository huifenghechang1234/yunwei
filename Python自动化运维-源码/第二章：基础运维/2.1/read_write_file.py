# -*- coding: utf-8 -*-

f = open("wb.txt", "w", encoding="utf-8")
f.write("测试w方式写入，如果文件存在，则清空内容后写入，如果文件不存在则创建\n")
f.close()

f = open("wb.txt", "a", encoding="utf-8")
f.write("测试a方式写入，如果文件存在，在文件内容后最后追加写入，如果文件不存在则创建")
f.close()

f = open("wb.txt", "r", encoding="utf-8")
# 以文本方式读，f.read()返回字符串对象
data = f.read()
print(type(data))
print(data)
f.close()

f = open("wb.txt", "rb")
# 以文本方式读，f.read()返回字节对象
data = f.read()
print(type(data))
print(data)
print('将读取的字符对象解码：')
print(data.decode('utf-8'))
f.close()
