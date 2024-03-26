# -*- coding: utf-8 -*-

import logging

# 创建logger,其名称为simple_example，名称为任意，也可为空
logger = logging.getLogger("lx_log2")
# 打印logger的名称
print(logger.name)
# 设置logger的日志级别
logger.setLevel(logging.INFO)

# 创建两个handler，一个负责将日志输出到终端，一个负责输出到文件，并分别设置他们的日志级别
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
fh = logging.FileHandler(filename="lx_log2.log", mode="a", encoding="utf-8")
fh.setLevel(logging.WARNING)
# 创建一个格式化器，可以创建不同的格式化器用于不同的handler，这里我们使用一个
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# 设置两个handler的格式化器
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# 为logger添加两个handler
logger.addHandler(ch)
logger.addHandler(fh)

# 在程序中记录日志
logger.debug("debug message")
logger.info("info message")
logger.warn("warn message")
logger.error("error message")
logger.critical("critical message")