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
MX记录 实现MX记录查询方法源码
"""

# 必须这样导入
import dns.resolver

print("-------------------------1--------------------------------------------------")
# 获取解析对象
ret = dns.resolver.query('dnspython.org', 'MX')
print(ret)
print("-------------------------1--------------------------------------------------")

print("-------------------------2--------------------------------------------------")
#
for data in ret:
    print(data)
print("-------------------------2--------------------------------------------------")

print("-------------------------3--------------------------------------------------")
#
for data in ret:
    print(data.exchange, data.preference)
print("-------------------------3--------------------------------------------------")


domain = '126.com'

print("------------------------------6---------------------------------------------")
# 获取解析对象
query_object = dns.resolver.query(domain, 'MX')  # MX记录
print('MX记录的结果：{}'.format(query_object))
print("------------------------------6---------------------------------------------")

print("------------------------------7---------------------------------------------")
# 从应答的response中获取查询记录
resp_object = query_object.response
print('MX记录的结果：{}'.format(resp_object))
print("------------------------------7---------------------------------------------")

print("------------------------------8---------------------------------------------")
# 从应答的answer中获取查询目录
answer_object = resp_object.answer
print('MX记录的结果：{}'.format(answer_object))
print("------------------------------8---------------------------------------------")

print("------------------------------9---------------------------------------------")
# 查看解析条目对象
answer_object = resp_object.answer
for query_item in answer_object:
    print('查看解析条目对象：{}'.format(query_item))
print("------------------------------9---------------------------------------------")

print("------------------------------10---------------------------------------------")
# 查看解析后的记录条目
query_item = resp_object.answer[0]
for item in query_item.items:
    print('解析后的记录条目条目：{}'.format(item))
print("------------------------------10---------------------------------------------")

print("------------------------------11---------------------------------------------")
# 查看解析后的记录条目-详细
query_item = resp_object.answer[0]
for item in query_item.items:
    print('邮件服务器权重：{}，邮件服务器地址：{}'.format(item.preference, item.exchange))
print("--------------------------------11-------------------------------------------")


print("-------------------------------12-------------------------------------------------------------")
# 导包
import dns.resolver

domain = '126.com'

query_object = dns.resolver.query(domain, 'MX')
for query_item in query_object.response.answer:
    for item in query_item.items:
        print('邮件服务器权重：{}，邮件服务器地址：{}'.format(item.preference, item.exchange))
print("---------------------------------12------------------------------------------")



print("--------------------------------13-------------------------------------------")
import dns.resolver

# 输入域名地址
domain = 'baidu.com'

# 指定查询类型为MX
MX = dns.resolver.query(domain, 'MX')

# 遍历回应结果，输出MX记录的preference及exchanger信息
for i in MX:
    print('MX preference=', i.preference, 'mail exchange=', i.exchange)
print("---------------------------------13------------------------------------------")

