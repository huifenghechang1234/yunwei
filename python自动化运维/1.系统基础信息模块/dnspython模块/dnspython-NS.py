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
NS记录 实现NS记录查询方法源码
        NS（Name Server）域名服务器记录。用来表明由哪台服务器对该域名进行解析。在注册域名时，
        总有默认的DNS服务器，每个注册的域名都是由一个DNS域名服务器来进行解析的。但是需要注意的
        是只能输入一级域名，如：baidu.com；对于二级以及多级域名，如www.baidu.com、wenku.baidu.com则是错误的
"""
# 导包
import dns.resolver

domain = '126.com'

NS = dns.resolver.query(domain, 'NS')
for i in NS.response.answer:
    for j in i.items:
        print(j.to_text())