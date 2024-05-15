"""
title = ''
author = 'huifenghechang'
mtime = '2024/3/9'
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

"""

import os
from ftplib import FTP


def ftp_makedirs(ftp, remote_path):
    """ 递归创建目录，同 os.makedirs()。"""
    ftp.cwd('/')  # 切换 FTP 根目录
    dires = remote_path.split('/')
    for dire in dires:  # 遍历给定路径的每一层目录
        try:
            ftp.cwd(dire)  # 切换给定路径的目录，如果没有，进入 except
        except:
            ftp.mkd(dire)  # 没有目录，创建后再切换，最终实现递归创建给定目录
            ftp.cwd(dire)


def ftp_path_exists(ftp, remote_path):
    """ 判断是否存在 ftp 路径，同 os.path.exists()，但是只能判断 dir，不能判断 file。"""
    try:
        ftp.cwd(remote_path)  # 能切换给定路径，说明存在
        return True
    except:
        return False


def ftp_file_exists(ftp, remote_file):
    """ 判断是否存在 ftp 文件，同 os.path.exists()，但是只能判断 file，不能判断 dir。"""
    try:
        ftp.size(remote_file)  # 能获取给定文件大小，说明存在
        return True
    except:
        return False


def get_local_path(local_path, file_list=None):
    """ 给定一个本地目录，递归获取所有文件。"""
    files = os.listdir(local_path)
    for file in files:
        if not os.path.isdir(local_path + os.sep + file):
            file_list.append(local_path + os.sep + file)
        else:
            if os.listdir(local_path + os.sep + file):
                get_local_path(local_path + os.sep + file, file_list)
    return file_list


def get_remote_path(ftp, remote_path, file_list=None):
    """ 给定一个 ftp 文件夹路径，获取路径下的所有文件。"""
    file_infos = []
    ftp.cwd(remote_path.replace('\\', '/'))  # 切换到下载目录
    ftp.dir(remote_path.replace('\\', '/'), file_infos.append)  # 列出文件夹内容，存入列表
    for file_info in file_infos:
        if file_info.startswith('-'):  # 以 - 开始，为文件
            file_list.append(remote_path + '\\' + file_info.split(' ')[-1])
        if file_info.startswith('d'):  # 以 d 开始，为文件夹
            folder = file_info.split(' ')[-1]
            get_remote_path(ftp, remote_path + '\\' + folder, file_list)
    return file_list


def upload_tracker(block, dst):
    """ 上传回调函数，实现上传进度。"""
    global write_size, total_size
    write_size += 64 * 1024  # 文件每次写入的大小，用来实现进度条，必须和 blocksize 大小一样
    progress = round((write_size / total_size) * 100)
    if progress >= 100:
        print('\rUpload ' + dst + ' ' + '100%', end='')
    else:
        print('\rUpload ' + dst + ' ' + '%3s%%' % str(progress), end='')


def upload_file(ftp, src, dst):
    """ 上传文件 """
    global write_size, total_size
    write_size = 0  # 文件每次写入的大小，初始为 0
    total_size = os.path.getsize(src.replace('\\', '/'))
    blocksize = 64 * 1024  # 文件每次写入缓冲区的大小，64 KB
    with open(src, "rb") as f:
        ftp.storbinary('STOR ' + dst.replace('\\', '/'), f, blocksize, lambda block: upload_tracker(block, dst))


def download_tracker(block, f, dst):
    """ 下载回调函数，实现上传进度。"""
    f.write(block)
    global write_size, total_size
    write_size += 64 * 1024
    progress = round((write_size / total_size) * 100)
    if progress >= 100:
        print('\rDownload ' + dst + ' ' + '100%', end='')
    else:
        print('\rDownload ' + dst + ' ' + '%3s%%' % str(progress), end='')


def download_file(ftp, src, dst):
    """ 下载文件。"""
    global write_size, total_size
    write_size = 0
    total_size = ftp.size(src.replace('\\', '/'))
    blocksize = 64 * 1024
    with open(dst, 'wb') as f:
        ftp.retrbinary('RETR ' + src.replace('\\', '/'), lambda block: download_tracker(block, f, dst), blocksize)


def upload(ftp, data):
    """ 处理上传，可以是文件列表或文件夹列表，不可以混合上传。"""
    if os.path.isfile(data["local_path"][0]):  # 上传列表中，第一个是文件且存在
        if not ftp_path_exists(ftp, data["remote_path"].replace('\\', '/')):
            ftp_makedirs(ftp, data["remote_path"].replace('\\', '/'))
        for filepath in data["local_path"]:
            dst = data["remote_path"] + '\\' + filepath.split('\\')[-1]
            upload_file(ftp, filepath, dst)
    elif os.path.isdir(data["local_path"][0]):  # 上传列表中，第一个是文件夹且存在
        if not ftp_path_exists(ftp, data["remote_path"].replace('\\', '/')):
            ftp_makedirs(ftp, data["remote_path"].replace('\\', '/'))
        file_list = []
        for local_path in data["local_path"]:
            file_list.extend(get_local_path(local_path, []))
        for filepath in file_list:
            dst = data["remote_path"] + '\\' + filepath.split('\\')[-1]
            upload_file(ftp, filepath, dst)


def download(ftp, data):
    """ 处理下载，可以下载文件列表或者文件夹列表，而不可混合下载。 """
    if not os.path.exists(data["local_path"]):
        os.makedirs(data["local_path"])
    if ftp_file_exists(ftp, data["remote_path"][0].replace('\\', '/')):  # 下载列表中，第一个是文件且存在
        for filepath in data["remote_path"]:
            dst = data['local_path'] + '\\' + filepath.split('\\')[-1]
            if ftp_file_exists(ftp, filepath.replace('\\', '/')):
                download_file(ftp, filepath, dst)
    elif ftp_path_exists(ftp, data["remote_path"][0].replace('\\', '/')):  # 下载列表中，第一个是文件夹且存在
        file_list = []
        for remote_path in data["remote_path"]:
            file_list.extend(get_remote_path(ftp, remote_path, []))
        for filepath in file_list:
            dst = data['local_path'] + '\\' + filepath.split('\\')[-1]
            if ftp_file_exists(ftp, filepath.replace('\\', '/')):
                download_file(ftp, filepath, dst)


if __name__ == '__main__':
    host, username, password = '*.*.*.*', '******', '******'
    ftp = FTP()
    ftp.encoding = "utf-8"
    ftp.connect(host)
    ftp.login(username, password)

    data1 = {"action": "upload", "local_path": ["C:\\test\\mayaFile\\ChenNan_Mod.ma"], "remote_path": "\\test1\\t1\\a1"}
    data = {"action": "download", "local_path": "C:\\test\\download\\a",
            "remote_path": ['\\test1\\t1\\a2\\ChenNan_Mod.ma']}
    print('Start...')
    if data["action"] == 'upload': upload(ftp, data1)
    if data["action"] == 'download': download(ftp, data)
    ftp.close()
    print('End...')
