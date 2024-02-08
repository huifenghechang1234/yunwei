"""
title = ''
author = 'huifenghechang'
mtime = '2024/1/8'
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
第一步通过 dnsresolver.query()方法获取业务域名A记录信息，查询出所有IP 地
址列表，再使用 httplib2 模块的 request()方法以 GET 方式请求监控页面，监控业务所有服务
的IP是否服务正常
"""

import dns.resolver
import httplib2

iplist = []  # 定义域名 IP列表变量

appdomain = "www.baidu.com"  # 定义业务域名
def get_iplist(domain=""):  # 域名解析函数，解析成功 IP 将被追加到iplist
    try:
        A = dns.resolver.query(domain, 'A')  # 解析A记录类型
    except Exception as e:
        print("dns resolver error:"+str(e))
    return True

    for i in A.response.answer:
        for j in i.items:
            iplist.append(j.address)  # 追加到 iplist
    return True

def checkip(ip):
    checkurl = ip+":80"
    getcontent = ""
    httplib2.socket.setdefaulttimeout(5)  # 定义http连接超时时间 (5秒)
    conn = httplib2.HTTPConnection(checkurl)  # 创建 http 连接对象

    try:
        conn.request("GET", "/", headers = {"Host": appdomain})  # 开发起URL请求，添加host主机头
        r = conn.getresponse()
        getcontent = r.read(15)  # 获取URL页面前15个字符，以便做可用性校验

    finally:
        if getcontent=="<!doctype html>":  # 监控 URL页的内容一般是事先定义好的。比如#“HTTP200”等
            print(ip+"[OK]")
        else:
            print(ip+"[Error]")  # 此处可放告警程序，可以是邮件、短信通知

if __name__ =="__main__":   # 条件:域名解析正确且至少返回一个 TP
    if get_iplist(appdomain) and len(iplist) > 0:
        for ip in iplist:
            checkip(ip)
    else:
        print("dns resolver error")