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
import logger

"""
日志输出-控制台和文件

format常用格式说明
%(levelno)s 打印日志级别的数值
%(levelname)s 打印日志级别名称
%(pathname)s 打印当前执行程序的路径，其实就是sys.argv[0]
%(filename)s 打印当前执行程序名
%(funcName)s 打印日志的当前函数
%(lineno)s 打印日志的当前行号
%(asctime)s 打印日志的时间
%(thread)s 打印线程ID
%(threadName)s 打印线程名称
%(process)s 打印进程ID
%(message)s 打印日志信息
"""
import logging
import os.path
import time

# 定义handler的输出格式
# %(asctime)s：日志记录的时间。
# %(filename)s：产生日志记录的文件名。
# %(lineno)d：产生日志记录的行号。
# %(levelname)s：日志记录的级别。
# %(message)s：日志记录的消息
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")


ch = logging.StreamHandler()  # 只要在输入到日志中的第二步和第三步插入一个handler输出到控制台
ch.setLevel(logging.WARNING)  # 输出到console的log等级的开关
ch.setFormatter(formatter)

# 创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # 设置Logger的日志级别为DEBUG
logger.addHandler(ch)  # 将StreamHandler添加到Logger

# 创建一个handler，用于写入日志文件
rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
log_path = os.path.dirname(os.getcwd()) + '/Logs/'
log_name = log_path + rq + '.log'
logfile = log_name

# 使用logger.XX来记录错误,这里的"error"可以根据所需要的级别进行修改
try:
    with open('Logs/test1', 'rb'):
        pass
except (SystemExit, KeyboardInterrupt):
    # 如果捕获到 SystemExit 或 KeyboardInterrupt 异常，将其重新抛出
    raise
except Exception as e:
    # 捕获其他异常，并记录错误信息到日志中
    logger.error('Failed to open file', exc_info=True)
