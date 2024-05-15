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
linux文件之间的对比
"""

import difflib
filename1 = '/tmp/passwd'
filename2 = '/tmp/passwd1'

with open(filename1) as f1, open(filename2) as f2:
    content1 = f1.read().splitlines(keepends=True)
    content2 = f2.read().splitlines(keepends=True)

d = difflib.HtmlDiff()
htmlcontent = d.make_file(content1, content2)

with open('passwdDiff.html', 'w') as f:
    f.write(htmlcontent)
