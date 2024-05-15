"""
title = ''
author = 'huifenghechang'
mtime = '2024/3/2'
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
logging日志模块

文件日志步骤：
1创建一个 Logger 对象
logger=logging.getLogger()
2.创建 handler 对象用于分配日志的输出
file_handler=logging.FileHandler(log_file)
3定制日志格式
file_handler.setFormatter(formatter) 
formatter = logging.Formatter("日志格式")
4应用到 handler 对象
logger.addHandler(file_handler)
5测试效果
logger.warning("打印日志")
"""

import logging

# 1.创建一个logger（日志记录器）对象；
my_logger = logging.Logger("first_logger")

# 2.定义handler（日志处理器），决定把日志发到哪里；
my_handler = logging.FileHandler('test.log')

# 3.设置日志级别（level）和输出格式Formatters（日志格式器）；
my_handler.setLevel(logging.INFO)
my_format = logging.Formatter("时间:%(asctime)s 日志信息:%(message)s 行号:%(lineno)d")

# 把handler添加到对应的logger中去。
my_handler.setFormatter(my_format)
my_logger.addHandler(my_handler)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  # logging.basicConfig函数对日志的输出格式及方式做相关配置

# 使用：
# 由于日志基本配置中级别设置为DEBUG，所以一下打印信息将会全部显示在控制台上
logging.basicConfig(level=logging.DEBUG)  # 设置默认打印日志级别
logging.info('this is a loggging info message')
logging.debug('this is a loggging debug message')
logging.warning('this is loggging a warning message')
logging.error('this is an loggging error message')
logging.critical('this is a loggging critical message')
my_logger.info("我是日志组件")
