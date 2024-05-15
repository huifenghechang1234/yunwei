"""
title = ''
author = 'huifenghechang'
mtime = '2023/12/28'
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
pyclamd模块
通过ClamdNetworkSocket()方法实现与业务服务器建立扫描socket连接,再通过启动
不同扫描方式实施病毒扫描并返回结果

多线程案例

环境前提：
1.clamd服务必须开启
2.由于是远程操作，所以必须是网络模式启动clamd服务
3.连接的时候使用NetworkSocket模式

多线程和单线程的代码区别
1.类构造函数，不需要Thread改造
2.任务的执行方式，不需要start()和join()
3.信息的输出，需要自己来实现

操作步骤:
1定制专用的日志配置文件
2加载日志配器文件
3希望输出信息的位置进行日志的输出
正常的信息用info、病毒信息用critical、连接失败用error
"""

import time
import pyclamd
from threading import Thread  # 1.导入多线程模块
import logging.config
import logging
from watchdog.observers import Observer
from watchdog.events import *
import os


class Scan(Thread):
    def __init__(self, IP, scan_type, file):  # 为保证每个线程都能正常的检查为每个对象都自动创建基本的属性
        """构造方法,参数初始化"""
        Thread.__init__(self)  # 改造对象的启动方式为线程方式
        self.IP = IP  # 定义多个传参数据、地址、扫描类型、扫描对象
        self.scan_type = scan_type
        self.file = file
        self.connstr = ""  # 定义两个额外的属性，两个临时存储的空间
        self.scanresult = ""

    def run(self):  # 1.定义多线程使用的run方法
        """多线程run方法"""
        try:
            cd = pyclamd.ClamdNetworkSocket(self.IP, 3310)  # 2.创建连接对象
            if cd.ping():  # 连通性检查    3. 连接正常才进行逻辑操作
                self.connstr = self.IP + " connection [OK]"  # 此处的connstr表示连接对象的状态信息
                cd.reload()  # 重载clamd病毒特征库，建议更新病毒库后做reload()操作
                if self.scan_type == "contscan_file":  # 选择不同的扫描方式  选择不同的模式使用对应的方法来进行操作
                    self.scanresult = "{0}\n".format(cd.contscan_file(self.file))  # 批量扫描
                elif self.scan_type == "multiscan_file":
                    self.scanresult = "{0}\n".format(cd.multiscan_file(self.file))  # 多线程扫描
                elif self.scan_type == "scan_file":
                    self.scanresult = "{0}\n".format(cd.scan_file(self.file))  # 及时扫描  此处的scanresult代表扫描后的结果信息
                time.sleep(1)  # 线程挂起1s
            else:  # 4.连接异常，返回连接对象状态信息
                self.connstr = self.IP + " ping error,exit"
                return
        except Exception as e:  # 5.连接对象创建失败，返回连接对象状态信息
            self.connstr = self.IP + " " + str(e)

        else:
            if self.scanresult.strip() == 'None':
                logging.info('{} 文件没有病毒'.format(self.file))
                # print('is None')

            else:
                # print('Not None')
                if 'FOUND' in self.scanresult:
                    # print('Found!')
                    logging.critical('{} 文件有病毒！！！快删除'.format(self.file))
                else:
                    # print('Access')
                    logging.error('%s 文件访问被拒绝！' % self.file)


def scanfile(file):
    # 1.定义基本的扫描属性
    IPs = ['192.168.0.99', 'x.x.x.x']  # 扫描主机列表
    scantype = "multiscan_file"  # 指写扫描模式，支持multiscan_file、contscan_file、scan_file
    scanfile = "/data/www"  # 指定扫描路径
    i = 1  # 1.2  设定临时的初始变量值

    # 定义多线程扫描的基本线程属性
    threadnum = 2  # 指定启动的线程数
    scanlist = []  # 存储扫描Scan类线程对象列表

    for ip in IPs:

        # 3.由于类是基于线程方式操作，所以可以放到多任务列表
        currp = Scan(ip, scantype, scanfile)  # 创建扫描Scan类对象，参数（IP,扫描模式，扫描路径）
        scanlist.append(currp)  # 追加对象到列表

        if i % threadnum == 0 or i == len(IPs):  # 当达到指定的线程数或IP列表数后启动、退出线程
            for task in scanlist:
                task.start()  # 启动线程  4.start()是多线程的启动方式，代表执行的类对象的run方法

            for task in scanlist:
                # 5.多线程执行完毕后结果的输出
                task.join()  # 到等待所有子线程退出，并输出扫描结果
                print(task.connstr)  # 打印服务器连接信息
                print(task.scanresult)  # 打印扫描结果
            scanlist = []  # 6，当所有的ip扫描完毕后，清空扫描列表
        i += 1  # 7.每扫描一次，就进行下一个IP的扫描


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # print("文件被修改了 {}".format(event.src_path))
        file = event.src_path
        print(file)
        if os.path.isfile(file):
            if '/.' not in file:
                logging.info('文件被修改或者创建了 :{}'.format(file))
                scanfile(file)


if __name__ == '__main__':
    path = "/home/python/code/prod"
    logging.config.fileConfig('logconfig.ini')
    logger = logging.getLogger('root')

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()
    observer.join()

"""
2.执行结果:
[root@mankel py] python3 test_main.py 
192.168.0.99 connection [OK]
None

3.生成病毒特征文件:
通过EICAR()方法生成一个带有病毒特征的文件/tmp/EICAR:代码如下
[root@mankel py] python3.
>>> import pyclamd
>>> cd = pyclamd.ClamdAgnostic()
>>> void = open('/tmp/EICAR','wb').write(cd.EICAR())

4.查看病毒特征文件
生成带有病毒特征的字符串内容如下,复制文件到目标主机的扫描目录当中,以便进行测试
[root@mankel py] cat /tmp/EICAR 
X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*
[root@mankel py] cp /tmp/EICAR /data/www/

5.启动扫描程序,感受区别
在本次实践过程中启用两个线程,可以根据目标主机数量,随意修改,代码运行结果如下:
[root@mankel py] python3 test_main.py 
192.168.0.99 connection [OK]
{'/data/www/EICAR': ('FOUND', 'Win.Test.EICAR_HDB-1')}
"""
