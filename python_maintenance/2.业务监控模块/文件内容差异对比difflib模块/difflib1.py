"""
title = ''
author = 'huifenghechang'
mtime = '2023/12/10'
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
    difflib模块实现两个字符串的差异对比，然后以版本控制风格输出
"""
# 1.导包
import difflib

# 2.准备字符内容
text1 = '''  1. Beautiful is better than ugly.
       2. Explicit is better than implicit.
       3. Simple is better than complex.
       4. Complex is better than complicated.
		'''
# 3.对字符进行简单切割
text1_line = text1.splitlines(keepends=True)

text2 = '''  1. Beautiful is better than ugly.
       3.   Simple is better than complex.
       4. Complicated is better than complex.
       5. Flat is better than nested.
     '''
text2_line = text2.splitlines(keepends=True)

# 4.创建differ对象
d = difflib.Differ()

# 5.调用compare()方法比较内容
differ_result = d.compare(text1_line, text2_line)

# 6.拼接比较后的效果
result_message = "\n".join(differ_result)
print("字符对比结果:{}".format(result_message))
# print(''.join(list(d.compare(text1_line, text2_line))))


print("----------------------------------------------------------------")
# 用html方式对比
# HtmlDiff()类的make_file()方法.作用是生成美观的HTML文档
import difflib

text1 = '''  1. Beautiful is better than ugly.
       2. Explicit is better than implicit.
       3. Simple is better than complex.
       4. Complex is better than complicated.
		'''.splitlines(keepends=True)

text2 = '''  1. Beautiful is better than ugly.
       3.   Simple is better than complex.
       4. Complicated is better than complex.
       5. Flat is better than nested.
     '''.splitlines(keepends=True)

# 创建htmldiff对象
d = difflib.HtmlDiff()

# 调用make_file方法进行比较
htmlContent = d.make_file(text1, text2)
# print(htmlContent)

# 打开文件内容
with open('diff.html', 'w') as f:
    f.write(htmlContent)


print("----------------------------------------------------------------")
# 用table方式对比
# HtmlDiff()类的make_table()方法.作用是生成美观的HTML文档表格方式
import difflib

text1 = '''  1. Beautiful is better than ugly.
       2. Explicit is better than implicit.
       3. Simple is better than complex.
       4. Complex is better than complicated.
		'''.splitlines(keepends=True)

text2 = '''  1. Beautiful is better than ugly.
       3.   Simple is better than complex.
       4. Complicated is better than complex.
       5. Flat is better than nested.
     '''.splitlines(keepends=True)

# 创建htmldiff对象
d = difflib.HtmlDiff()

# 调用make_file方法进行比较
htmlContent = d.make_table(text1, text2)
# print(htmlContent)

# 打开文件内容
with open('diff_table.html', 'w') as f:
    f.write(htmlContent)