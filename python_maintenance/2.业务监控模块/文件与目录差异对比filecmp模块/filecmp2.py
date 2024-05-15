"""
title = ''
author = 'huifenghechang'
mtime = '2023/12/27'
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
filecmp.cmpfiles(a, b, common, [shallow])，用于比较两个目录。a, b为目录路径，
common为比较文件列表，shallow为可选参数，如果其值为True，则仅比较文件的元数据，即文
件的os.stat()签名(如大小，修改日期等)，如果它们具有相同的签名，则无论文件内容如何，
文件都被视为相等。如果为False，则比较文件的内容。此参数的默认值为True
"""

import filecmp

"""
说明：
dir1中有三个文件，"text.txt", "text1.txt", "text2.txt"
dir2中有两个文件，"text.txt", "text1.txt"
两个文件夹中的"text.txt"文件一样，"text1.txt"文件不一样
"""
dir1 = r'K:\PythonProject\wsw\floder1'
dir2 = r'K:\PythonProject\wsw\folder'
common_list = ["text.txt", "text1.txt", "text2.txt"]
match, mismatch, errors = filecmp.cmpfiles(dir1, dir2, common_list, shallow=True)

print("比较的结果中，匹配的是：\n{}\n不匹配的是：\n{}\n错误的是：\n{}\n".format(match, mismatch, errors))



























