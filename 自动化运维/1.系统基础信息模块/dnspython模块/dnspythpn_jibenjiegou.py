"""
title = ''
author = 'huifenghechang'
mtime = '2024/1/7'
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
dnspython模块的基本结构
"""

import dns.resolver

domain = 'www.baidu.com'
dns_type = 'A'

# 获取解析对象
query_object = dns.resolver.query(qname=domain, rdtype=dns_type)  # 指定查询记录为A
print('查询对象：{}'.format(query_object))    # <dns.resolver.Answer object at 0x000001B27449AA90>

print('*' * 100)

# 查看response对象
response_object = query_object.response
print('应答对象：{}'.format(response_object))

print('*' * 100)

# 查询answer对象
answer_object = response_object.answer
print('解析对象：{}'.format(answer_object))    # [<DNS www.baidu.com. IN A RRset>]

print('*' * 100)

# 查看解析条目对象
answer_object = response_object.answer
for query_item in answer_object:
    print('查询条目：{}'.format(query_item))  # 查询条目：www.baidu.com. 219 IN A 183.2.172.42   www.baidu.com. 219 IN A 183.2.172.185

print('*' * 100)

# 解析后的记录条目
query_item = response_object.answer[0]
# print(query_item)
for item in query_item.items:
    print('解析记录：{}'.format(item))   # 解析记录：183.2.172.42   解析记录：183.2.172.185

print('*' * 100)