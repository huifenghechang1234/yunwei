"""
title = ''
author = 'huifenghechang'
mtime = '2023/12/17'
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
import difflib
import sys

try:
    textfilel = sys.argv[1]   # 第一个配置文件路径参数
    textfile2 = sys.argv[2]   # 第二个配置文件路径参数

except Exception as e2:
    print("Error:" + str(e2))
    print("Usage: differ4_programe.py flename1 filename2")
    sys.exit()

# 文件读取分隔函数
def readfile(filename):
    try:
        # with open(filename, "r") as f:
        #     text = f.read().splitlines()
        #     return text

        fileHandle = open(filename, 'rb')  # 读取后以行进行分隔
        text = fileHandle.read().splitlines()
        fileHandle.close()
        return text
    except IOError as e1:
        print('Read file Error:' + str(e1))
        sys.exit()

# 参数位置为空的基本判断
if textfilel == "" or textfile2 == "":
    print("脚本的参数不允许为空，请检查")
    print("Usage: differ4_programe.py filenamel filename2")
    sys.exit()

# 读取文件
text1_lines = readfile(textfilel)   # 调用readfile函数，获取分隔后的字符串
text2_lines = readfile(textfile2)

# 创建HtmlDiff()类对象
d = difflib.HtmlDiff()

# 通过makefile方法输出HTML格式的比对结果
diff_result =print(d.make_file(text1_lines, text2_lines))

# 结果输出
with open("file.html", 'r') as f:
    f.write(diff_result)

