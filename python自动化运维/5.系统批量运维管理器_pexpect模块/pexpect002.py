"""
title = ''
author = 'huifenghechang'
mtime = '2024/3/17'
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
FTP文件管理
"""

import pexpect, sys, os, re, time
def login_ftp():
    ftp = pexpect.spawn('ftp', cwd = cwd)
    if ftp.expect(prmpt) != 0:
        sys.exit()
    ftp.sendline('open {ip} {port}'.format(ip = ip, port = port))
    if ftp.expect('Name') != 0:
        sys.exit()
    ftp.sendline(username)
    if ftp.expect('Password:') != 0:
        sys.exit()
    ftp.sendline(password)
    if ftp.expect('230') != 0 or ftp.expect(prmpt) != 0:
        sys.exit()
    return ftp

def get_server_files(ftp):
    ftp.sendline('ls')
    if ftp.expect('226') != 0:
        sys.exit()
    file_list = ftp.before
    file_list = file_list.split('\n')
    remtch = re.compile('\s+')
    file_list = [remtch.subn(' ', item.strip('\r'))[0] for item in file_list if 'group' in item]
    file_dict = dict()
    for item in file_list:
        datas = item.split(' ')
        file_dict[datas[-1]] = {'mon': week.index(datas[-4]) + 1, 'day': int(datas[-3]), 'time': datas[-2]}
    return file_dict

def get_local_files():
    local_files = os.listdir(cwd)
    local_files_dict = dict()
    for file in local_files:
        t = time.ctime(os.stat(os.path.join(cwd, file)).st_mtime)
        datas = t.split(' ')
        local_files_dict[file] = {'mon': week.index(datas[-4]) + 1, 'day': int(datas[-3]), 'time': datas[-2][:5]}
    return local_files_dict

def sync_files(ftp, local_files, remote_files):
    add_file = []
    for file in local_files.keys():
        if file not in remote_files:
            add_file.append(file)
        if file in remote_files:
            if local_files[file]['mon'] > remote_files[file]['mon']:
                add_file.append(file)
    if add_file:
        for f in add_file:
            ftp.sendline('put' + f)
            if ftp.expect(['226', pexpect.EOF]) == 0:
                print('upload success: ', f)
            else:
                sys.exit()
    # 以下代码会删除FTP服务器上的文件，测试请慎重
    # delete_files = set(remote_files.keys()) - set(local_files.keys())
    # if delete_files:
    #     for f in delete_files:
    #         ftp.sendline('delete' + f)
    #         if ftp.expect(['250', pexpect.EOF]) == 0:
    #             print('delete success: ', f)
    #         else:
    #             print('Permision denied')
    #             sys.exit()

def exit_ftp(ftp):
    if ftp:
        ftp.sendcontrol('d')
        print(ftp.read().decode())

if __name__ == '__main__':
    week = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
    cwd = '/root/backup'
    prmpt = ['ftp>', pexpect.EOF]
    ip = '172.17.2.76'
    port = '2121'
    username = 'xxxxx'
    password = 'xxxxxx'

    ftp = login_ftp()
    remote_files = get_server_files(ftp)
    print(remote_files)
    print('=' * 50)
    local_files = get_local_files()
    print(local_files)
    exit_ftp(ftp)
