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
转储YAML
yaml.dump 函数接受一个Python对象并生成一个YAML文档
"""
import yaml
emp_info = {'name': 'Lex',
'department': 'SQA',
'salary': 8000,
'annual leave entitlement': [5, 10]
}
print(yaml.dump(emp_info))
# annual leave entitlement: [5, 10]
# department: SQA
# name: Lex
# salary: 8000


