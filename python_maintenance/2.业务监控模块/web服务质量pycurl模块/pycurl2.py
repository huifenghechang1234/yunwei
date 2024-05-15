# """
# title = ''
# author = 'huifenghechang'
# mtime = '2023/12/27'
# code is far away from bugs with the god animal protecting
# I love animals. They taste delicious.
# ┏┓      ┏┓
# ┏┛┻━━━┛┻┓
# ┃      ☃      ┃
# ┃  ┳┛  ┗┳  ┃
# ┃      ┻      ┃
# ┗━┓      ┏━┛
# ┃      ┗━━━┓
# ┃  神兽保佑    ┣┓
# ┃　永无BUG！   ┏┛
# ┗┓┓┏━┳┓┏┛
# ┃┫┫  ┃┫┫
# ┗┻┛  ┗┻┛
# """
"""
探测web服务质量

衡量服务子类的标准：
1.服务的可用性，是否处于正常提供服务状态
2.服务的响应速度

操作步骤：
1.创建对象
2.设定属性
3.发起请求
4.关闭请求
"""

import pycurl
import os, sys


def getInfo(URL):
    """
    :param URL:用户输入需要检测的URL地址
    info 字典主要用于映射dic字典
    dic字典主要存下curl结果
    :return:没return，直接print，函数可以改写，可以用于定时检测多个域名，增加一个需要检测的url列表即可
    """
    # 创建对象
    c = pycurl.Curl()

    # 设定请求属性
    c.setopt(pycurl.URL, URL)  # 定义请求的URL常量
    c.setopt(pycurl.CONNECTTIMEOUT, 5)  # 请求等待时间最多5秒
    c.setopt(pycurl.TIMEOUT, 5)  # 定义请求超时时间（服务器没回应）
    c.setopt(pycurl.NOPROGRESS, 1)  # 屏蔽下载进度条
    c.setopt(pycurl.FORBID_REUSE, 1)  # 交互完成后强制断开连接，不重用
    c.setopt(pycurl.MAXREDIRS, 1)  # 指定HTTP重定向的最大数为1
    c.setopt(pycurl.DNS_CACHE_TIMEOUT, 30)  # 设置DNS信息保存时间为30秒
    c.setopt(pycurl.USERAGENT,
             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 OPR/40.0.2308.81 (Edition Baidu)")

    dic = {}  # 定义一个空字典

    info = {'NAMELOOKUP_TIME': 'DNS解析时间', 'CONNECT_TIME': '建立连接时间',
            'PRETRANSFER_TIME': '建立到准备传输所消耗的时间', 'STARTTRANSFER_TIME': '建立连接到传输开始消耗的时间',
            'TOTAL_TIME': '传输总时间',
            'HTTP_CODE': 'HTTP状态码', 'SIZE_DOWNLOAD': '下载数据包大小', 'HEADER_SIZE': 'HTTP头部大小',
            'SPEED_DOWNLOAD': '平均下载速度'}  # 字典

    with open(os.path.dirname(os.path.realpath(__file__)) + "/content.txt", "wb") as indexfile:
        # indexfile 是一个变量名，它是程序中的一个标识符，用于表示一个文件对象，indexfile 代表被打开的文件对象，用于操作名为 "content.txt" 的文件
        c.setopt(pycurl.WRITEHEADER, indexfile)  # 将返回的HTTP HEADER头部信息定向到indexfile文件对象
        c.setopt(pycurl.WRITEDATA, indexfile)  # 将返回的HTML内容定向到indexfile文件对象
        try:
            c.perform()  # 这一行执行 pycurl 对象 c 的网络请求。它会发起网络请求并等待响应
        except Exception as e:
            print("Connection error:" + str(e))
            indexfile.close()
            c.close()
            sys.exit()  # 这一行退出程序。在发生连接错误时，程序将会被终止

        dic['NAMELOOKUP_TIME'] = '%.2f ms' % (c.getinfo(c.NAMELOOKUP_TIME) * 1000)  # 获取DNS解析时间
        dic['CONNECT_TIME'] = '%.2f ms' % (c.getinfo(c.CONNECT_TIME) * 1000)  # 获取建立连接时间
        dic['PRETRANSFER_TIME'] = '%.2f ms' % (c.getinfo(c.PRETRANSFER_TIME) * 1000)  # 获取从建立到准备传输所消耗的时间
        dic['STARTTRANSFER_TIME'] = '%.2f ms' % (c.getinfo(c.STARTTRANSFER_TIME) * 1000)  # 获取从建立连接到传输开始消耗的时间
        dic['TOTAL_TIME'] = '%.2f ms' % (c.getinfo(c.TOTAL_TIME) * 1000)  # 获取传输总时间
        dic['HTTP_CODE'] = c.getinfo(c.HTTP_CODE)  # 获取HTTP状态码
        dic['SIZE_DOWNLOAD'] = '%d bytes/s' % (c.getinfo(c.SIZE_DOWNLOAD))  # 获取下载数据包大小
        dic['HEADER_SIZE'] = '%d bytes/s' % (c.getinfo(c.HEADER_SIZE))  # 获取HTTP头部大小
        dic['SPEED_DOWNLOAD'] = '%d bytes/s' % (c.getinfo(c.SPEED_DOWNLOAD))  # 获取平均下载速度

    # 对于字典 info 中的每个键，打印出 info 字典中相应键的值，后跟一个分隔符 ':'，然后打印出另一个字典 dic 中相应键的值
    for key in info:
        print(info[key], ':', dic[key])


def main():
    while True:
        URL = input("请输入一个URL地址(Q for exit)：")
        if URL.lower() == 'q':
            sys.exit()  # 退出程序
        else:
            getInfo(URL)


if __name__ == '__main__':
    main()
