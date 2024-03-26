"""
title = ''
author = 'huifenghechang'
mtime = '2024/3/11'
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
操作步骤
整体来说大致的流程包括:
1 spawn - 根据需求创建一个执行命令的程序
2 expect - 通过关键字匹配中断的位置
3 send - 根据关键字向程序发送符合的字符

注意：第一步只需要做一次，后面两步根据实际需要多次执行
"""

# 1导包
import pexpect

# 2 创建连接对象
child = pexpect.spawn('ssh python@192.168.8.12 ifconfig', encoding='utf-8')

# 3-1以加模式打开文件
fout = open('mylog.txt', 'a')
# 此处可以使用”wb"
# 3-2为连接对象附加1ogfile属性
child.logfile = fout

# 4获取期望标识并发送对应信息
child.expect('password:')
child.sendline('123456')
child.expect('python@python-auto')
child.sendline('1s /tmp')

# 5 期望获取pexpect的执行结束标识
# child.expect(pexpect.EOF)
# 由于我们这里将信息记录到文件，默认这里的EOF会有超时等待，所以将该行代码禁用了

# 6 查看执行的信息
with open('mylog.txt', 'r') as f:
    content = f.read()
    print(content)
