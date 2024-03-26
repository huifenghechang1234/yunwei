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
dns.resolve源码解析:
def query(qname, rdtype=dns.rdatatype.A, rdclass=dns.rdataclass.IN,
          tcp=False, source=None, raise_on_no_answer=True,
          source_port=0)
          
参数解析：
qname 指定查询的名称
rdtype 指定查询的类型 默认是A记录
rdclass 指定查询的网络类型 ,可选的值有IN、CH与HS,默认是 IN
tcp 是否启用tcp查询模式
source 和source_port 指定 查询用的源地址和端口
raise_on_no_answer 查询无结果的时候，是否需要抛出异常
lifetime 声明周期配置参数，采用默认值

rdtype 指定查询的类型,默认是A记录:
A记录，将主机名转换为IP地址；
MX记录，邮件交换记录，定义邮件服务器的域名；
CNAME记录，指别名记录，实现域名间的映射；
NS记录，标记区域的域名服务器及授权子域；
PTR记录，反向解析，与A记录相反，将IP转换为主机名；
SOA记录，SOA标记，一个起始授权区的定义
"""

"""
A记录  实现A记录查询方法源码
"""

# 导包
import dns.resolver


print('*' * 100)
domain1 = input('Please input an domain: ') # 输入域名地址

A1 = dns.resolver.query(domain1, 'A')  # 指定查询类型为A记录
for i in A1.response.answer:   # 通过 response.answer 方法获取查询回应信息
    for j in i.items:  # 遍历回应信息
        if j.rdtype == 1:  # 加判断，不然会出现AttributeError: 'CNAME' object has no attribute 'address'
            print("{}的A记录解析结果有：{}".format(domain1, j.address))
print('*' * 100)


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




print("---------------------------1-------------------------------------")
# 导包
import dns.resolver

domain = 'www.baidu.com'

query_object = dns.resolver.query(qname=domain, rdtype='A')
for query_item in query_object.response.answer:
    for item in query_item.items:
        print("{}的A记录解析地址有：{}".format(domain, item))
print("--------------------------1--------------------------------------")




print("-------------------------2---------------------------------------")
import dns.resolver

domain = 'www.baidu.com'
# 指定查询类型为A记录
A = dns.resolver.query(domain, 'A')
# 通过response.answer方法获取查询信息
for i in A.response.answer:
    print('+' * 100)
    print(i)
    # 遍历回应信息
    for j in i.items:
        print(j)
    print("*" * 100)
print("----------------------------2------------------------------------")





















