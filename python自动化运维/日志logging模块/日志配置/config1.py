"""
title = ''
author = 'huifenghechang'
mtime = '2024/3/3'
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
Python的logging模块提供了config()方法，用于从字典配置或配置文件中配置日志系统的行为。
该方法允许你通过字典、INI文件、JSON文件或者YAML文件等方式来配置日志记录器、处理器、过滤器和格式器等参数

定义了一个字典类型的配置logging_config，该配置包含了日志系统的各种参数，包括了日志记录器、处理器、过滤器和
格式器等的配置。然后，我们使用dictConfig()方法加载这个配置，将其应用到日志系统中。

通过使用config()方法，你可以通过字典、INI文件、JSON文件或者YAML文件等方式来配置日志系统的行为，使得日志配置
更加灵活和方便
"""

import logging.config

# 配置日志记录器、处理器、过滤器和格式器等参数的字典配置
logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'example.log',
            'level': 'INFO',
            'formatter': 'standard'
        },
        'console_handler': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'standard'
        },
    },
    'loggers': {
        '': {
            'handlers': ['file_handler', 'console_handler'],
            'level': 'DEBUG',
            'propagate': True
        }
    }
}

# 使用字典配置方式配置日志系统
logging.config.dictConfig(logging_config)

# 获取Logger
logger = logging.getLogger()

# 记录日志消息
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
