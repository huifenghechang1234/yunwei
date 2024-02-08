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
本示例使用了 filec mp 模块的 le ft_only、山ff_files 方法递归获取源目录的更新项 ，再通过shutil.copyfile 、
os.makedir s 方法对更新项进行复制， 最终保持一致状态
"""

import os ,sys
import filecmp
import re
import shutil
from os.path import abspath

holderlist = []
# 递归获取更新项函数

def compareme (dir1, dir2):
    dircomp = filecmp.dircmp(dir1, dir2)
    only_in_one = dircomp.left_only  # 源目录新文件或目录
    diff_in_one = dircomp.diff_files  # 不匹配文件，源目录文件已发生变化
    dirpath = os.path.abspath(dir1)     #定义源目录绝对路径

#将更新文件名或目录追加到 holderlist
    [holderlist.append(os.path.abspath(os.path.join(dir1,x))) for x in only_in_one]
    [holderlist.append(os.path,abspath(os.path.join(dir1,x))) for x in diff_in_one]  #并判断是否存在相同子目录，以便递归
#递归子目录
    if len(dircomp.common_dirs) > 0:
        for item in dircomp .common_dirs:
            compareme(os.path.abspath(os.path.join(dir1,item)),
            os.path.abspath(os.path.join(dir2,item)))
        return holderlist

def main():
    if len(sys.argv) > 2:   #要求输入源目录与备份目录
        dir1=sys.argv[1]
        dir2=sys.argv[2]
    else:
        print("Usage:",sys.argv[0],"datadir backupdir")
        sys.exit()

    source_files=compareme(dir1,dir2)  # 对比源目录与备份目录
    dir1=os.path.abspath(dir1)

# 备份目录路径加“/”符
    if not dir2.endswith('/'): dir2=dir2+'/'
    dir2=os.path.abspath(dir2)
    destination_files=[]
    createdir_bool=False

    for item in source_files:  # 遍历返回的差异文件或目录清单
        destination_dir=re.sub(dir1,dir2,item)   # 将源目录差异路径清单对应替换成
                                                    # 备份目录
        destination_files.append(destination_dir)

        if os.path.isdir(item):    # 如果差异路径为目录且不存在，则在备份目录中创建
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
                createdir_bool=True  # 再次调用 compareme 函数标记

        if createdir_bool:    #重新调用 compareme函数，重新遍历新建目录的内容
            destination_files=[]
            source_files=[]
            source_files=compareme(dir1,dir2)  #调用 compareme 函数

            for item in source_files:   # 获取源目录差异路径清单，对应替换成备份目录
                destination_dir=re.sub(dir1, dir2,item)
                destination_files.append(destination_dir)
        print("update item:")  # 输出更新项列表单
        print(source_files)
        copy_pair=zip(source_files,destination_files) # 将源目录与备份目录文件清单拆分成元组
        for item in copy_pair:
            if os.path.isfile(item[0]):  # 判断是否为文件，是则进行复制操作
                shutil.copyfile(item[0],item[1])

if __name__ == '__main__':
    main()
