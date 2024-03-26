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
案例分析：DNS域名轮询业务监控
大部分的DNS解析都是一个域名对应一个IP地址，但是通过DNS轮询技术可以做到一个域名对应多个IP，从而实现最简单高效的负载均衡，不过此方案最大的弊端是目标主机不可用时无法被自动剔除，因此做好业务主机的服务可用监控至关重要。

实现步骤：

实现域名的解析，获取域名所有的A记录解析IP列表
对IP列表进行HTTP级别的探测
具体实现方式：

第一步通过dns.resolver.query()
方法获取业务域名A记录信息，查询出所有IP地址列表；

第二步使用httplib模块的request()
方法以GET请求监控页面，监控业务所有服务的IP是否正常。
"""

import dns.resolver
import http.client

# 定义域名ip列表变量
ip_list = []
# 定义业务域名
app_domain = "www.baidu.com"


# app_domain = "www.blog.csdn.net"


# 域名解析函数，解析成功IP将被追加到ip_list
def get_ip_list(domain=""):
    try:
        A = dns.resolver.query(domain, 'A')
    except Exception as e:
        print("dns resolver error: " + str(e))
        return
    for i in A.response.answer:
        for j in i.items:
            # 追加到ip_list列表
            ip_list.append(j)
    return True


def check_ip(ip):
    check_url = str(ip) + ": 80"
    get_content = ""
    # 定义http连接5秒超时(5)秒
    http.client.socket.setdefaulttimeout(5)
    # 创建http连接对象
    conn = http.client.HTTPConnection(check_url)
    try:
        # 发起url请求，添加host主机头
        conn.request("GET", "/", headers={"Host": app_domain})
        r = conn.getresponse()
        # 获取URL页面前15个字符用来可用性效验
        get_content = r.read(15)
    finally:
        # 监控URL页的内容一般是事先定义好的比如http 200等
        # 判断是否为字节
        if isinstance(get_content, bytes):
            get_content = get_content.decode('utf-8')
        if get_content == "<!DOCTYPE html>":
            print(str(ip) + "\033[32;1m [ok]\033[0m")
        else:
            print(str(ip) + "\033[31;1m [Error]\033[0m")
        # 获取response的状态码
        print(r.reason)
        # 获取response的状态 ok或error
        print(r.status)


if __name__ == "__main__":
    # 域名解析正确且至少返回一个IP
    if get_ip_list(app_domain) and len(ip_list) > 0:
        for ip in ip_list:
            check_ip(ip)
    else:
        print("dns resolver error.")