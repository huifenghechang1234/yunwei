"""
title = ''
author = 'huifenghechang'
mtime = '2024/3/10'
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
    ftplib模块文件操作
"""

import os
import time
from ftplib import FTP


class MyFTP(object):
    def __init__(self, host, username, password):
        """设定连接服务器的基本信息"""
        self.host = host  # ip地址
        self.username = username  # 用户名
        self.password = password  # 密码
        self.port = 21  # 端口
        self.ftp = FTP()
        self.bufsize = 1024  # 文件传输过程中临时空间大小
        self.encoding = 'utf-8'  # 中文解码

    # 日志功能
    def write_log(self, log_str):
        """打印日志信息"""
        # 定制当前的日志时间格式
        date_now = time.strftime('%Y-%m-%d %H:%M', time.localtime())

        # 输出指定的信息
        print("{} -> {}".format(date_now, log_str))

    # 登录功能
    def ftp_connect(self):
        """连接ftp服务器"""
        try:
            # 连接ftp主机
            self.write_log('开始尝试连接到 {}：{}'.format(self.host, self.port))
            self.ftp.connect(self.host, self.port)  # 连接
            self.write_log('正在尝试连接到主机 {}:{}'.format(self.host, self.port))
            self.write_log('成功连接到主机 {}:{}'.format(self.host, self.port))

            # 登录ftp主机
            self.write_log('开始尝试登录到 {}：{}'.format(self.host, self.port))
            self.ftp.login(self.username, self.password)  # 登录，如果匿名登录则用空串代替即可
            self.write_1og('成功登录到 {}:{}'.format(self.host, self.port))
            self.write_log(self.ftp.welcome)

        except Exception as e:
            self.write_log("FTP连接或登录失败: {}".format(e))
            return 500

    # 断开功能
    def ftp_close(self):
        """断开ftp服务器"""
        self.write_log('尝试断开{}服务器'.format(self.host))
        self.ftp.quit()
        self.write_log('成功断开 {} 服务器'.format(self.host))

    # 文件查看功能
    def file_name(self, path=None):
        # 借助于现有的ftp对象进行文件内容查看
        if path:
            self.write_log('查看 {} 路径下面的文件名称'.format(path))
            self.ftp.nlst(path)
        else:
            path = self.ftp.pwd()
            self.write_log('查看 {} 路径下面的文件名称'.format(path))
            self.ftp.nlst()
            # print(self.ftp.nlst(path))
            for filename in self.ftp.nlst(path):
                print(filename)

    # 文件列表功能
    def file_list(self, path=None):
        # 借助于现有的ftp对象进行文件内容查看
        if path:
            self.write_log("查看 {} 路径下面的文件列表", format(path))
            self.ftp, dir(path)
        else:
            path = self.ftp.pwd()
            self.write_log("查看 路径下面的文件名称".format(path))
            self.ftp.dir()

    # 比较本地文件和远程文件功能
    def compare_file(self, remotefile, localfile):
        """比较本地和远程文件"""

        # 本地文件的查询
        try:
            local_file_size = os.path.getsize(localfile)
        except Exception as e:
            self.write_1og('本地文件获取失败，错误描述为:'.format(e))
            local_file_size = -1  # 这里的-1代表远程文件不存在

        # 远程文件的查询
        try:
            remote_file_size = os.path.getsize(localfile)
        except Exception as e:
            self.write_1og('远程文件获取失败，错误描述为:'.format(e))
            remote_file_size = -1  # 这里的-1代表本地文件不存在

        # 如果远程文件和本地文件存在的话，比较文件大小
        if local_file_size != -1 and remote_file_size != -1:
            self.write_log('远程文件大小:，本地文件大小:{}'.format(remote_file_size, local_file_size))

        # 防止文件内容一致的时候文件上传或下载
        if remote_file_size == local_file_size:
            return 1  # 这里的1表示后续上传或者下载的文件是否一致的判断

    # 2.7远程文件是否存在
    def remote_file_exist(self, file_path):
        if file_path:
            try:
                self.ftp.size(file_path)
            except:
                self.write_log("远程文件 {} 不存在".format(file_path))
                return 404  # 如果文件找不到的话，直接返回404

    # 2.8 本地文件是否存在
    def local_file_exist(self, file_path):
        if file_path:
            try:
                os.path.getsize(file_path)
            except:
                self.write_log("本地文件 {} 不存在".format(file_path))
                return 404  # 如果文件找不到的话，直接返回404

    # 下载远程文件
    def download_file(self, remotefile, localfile):
        """下载远程文件"""
        self.write_log('尝试下载远程文件{} 到本地 {}'.format(remotefile, localfile))
        result = self.compare_file(remotefile, localfile)

        if result:
            self.write_log('{} 文件大小相同，无需下载'.format(localfile))
        else:
            try:
                self.write_log('开始下载文件{}....'.format(remotefile))
                with open(localfile, "wb") as f:
                    self.ftp.retrbinary('RETR' + remotefile, f.write, self.bufsize)
                    self.write_log('下载文件{} 完毕'.format(remotefile))
            except Exception as e:
                self.write_log('下载文件出错，出现异常:{}'.format(e))

    # 删除远程文件
    def delete_file(self, file_path):
        """删除远程文件"""
        if file_path:
            self.write_log("开始删除 {} 文件".format(file_path))
            remote_status = self.remote_file_exist(file_path)
            if remote_status == 0:  # 删除远程文件的话,定要保证远程文件存在
                try:  # 防止权限之外的文件被删除，发生异常
                    self.ftp.delete(file_path)
                    self.write_log("删除 {} 文件成功", format(file_path))
                except Exception as e:
                    self.write_log("删除 {} 文件失败，错误信息如下: {}".format(file_path, e))
            else:
                self.write_log("您要删除的文件 {} 不存在".format(file_path))
        else:
            self.write_log("请输入您要删除的文件!!!")

    # 上传本地文件
    def upload_file(self, remote_file, local_file):
        """上传本地文件"""
        # 1 保证本地文件是存在的
        local_status = self.local_file_exist(local_file)
        if local_status == 0:
            # 2 判断本地文件和远程文件是否内容一致
            context_status = self.compare_file(remote_file, local_file)
            if context_status == 1:
                self.write_log("本地文件{} 和远程文件{} 内容，无需上传".format(local_file, remote_file))
            else:
                # 3 正常的文件上传操作
                with open(local_file, "rb") as f:
                    self.write_log("开始将本地文件{} 上传到远程文件".format(local_file, remote_file))
                    self.ftp.storbinary('STOR ' + remote_file, f, self.bufsize)
                    self.write_log("本地文件{} 上传到远程文件{} 成功".format(local_file, remote_file))
        else:
            self.write_log("本地文件 {} 不存在，无法上传".format(local_file))


if __name__ == "__main__":
    # 1 创建连接对象
    my_ftp = MyFTP("192.168.43.13", "python", "123456")
    # 2 连接ftp服务器
    result = my_ftp.ftp_connect()
    if result != 500:
        # my_ftp.download_file("fstab"，"/tmp/fstab") # 下载文件
        # my_ftp.delete_file("upload/fstab") # 删除文件
        my_ftp.upload_file("upload/fstab", "/tmp/fstab")  # 上传文件
        my_ftp.ftp_close()  # 断开连接
