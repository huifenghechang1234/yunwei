import logging
import logging.config

logging.config.fileConfig('logging.conf')

#  创建一个logger
logger = logging.getLogger('simpleExample')

# 日志记录
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')

