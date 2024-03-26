import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s",  # 日志的格式
    datefmt=" %Y-%m-%d %H:%M:%S",  # 时间格式
    filename="./lx_log1.log",  # 指定文件位置
    filemode="w",
)
logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")
