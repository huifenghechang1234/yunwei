"""
title = ''
author = 'huifenghechang'
mtime = '2023/11/30'
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
dnspython是python 实现的一个dns场景的工具包。

 dnspython（http://www.dnspython.org/）是Python实现的一个DNS工具包，它支持几乎所有的记录类型，
可以用于查询、传输并动态更新ZONE信息，同时支持TSIG（事务签名）验证消息和EDNS0（扩展DNS）。在系统管理
方面，我们可以利用其查询功能来实现DNS服务监控以及解析结果的校验，可以代替nslookup及dig等工具
"""

# 导包
import dns
import dns.resolver

#  domain = input("请输入域名地址:")  # 输入域名地址

domain = 'www.baidu.com'

# 2 获取解析对象
query_object = dns.resolver.Resolver(qname='domain', rdtype='A')  # 指定查询记录为A型
print("查询对象：{}".format(query_object))

# 3 查看response 对象
response_object = query_object.response
print("应答对象：{}".format(response_object))

# 4 查看answer对象
answer_object = response_object.answer
print("解析对象：{}".format(answer_object))

# 5 查看解析条目对象
answer_object = response_object.answer
for query_item in answer_object:
    print("查询条目：{}".format(query_item))
# 6 查询解析后的记录条目
query_item = response_object.answer[1]
for item in query_item.items:
    print("解析记录：{}".format(item))
# 7 查看解析后的记录条目
query_item = response_object.answer[1]
for item in query_item.items:
    print("解析地址：{}".format(item.address))



# import dns.resolver
# domain = input("请输入域名地址:")       # 输入域名地址
#
# query_object = dns.resolver.resolve(qname = domain, rdtype = 'A')
# for query_item in query_object.response.answer:
#     for item in query_item.items:
#         print("{}的A记录解析地址有：{}".format(domain,item))
