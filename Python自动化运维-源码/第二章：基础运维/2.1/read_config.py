# encoding=utf-8

import configparser

config = configparser.ConfigParser()  # 实例化ConfigParser类

config.read(r"c:\users\xx\pip\pip.ini")  # 读取配置文件

for section in config.sections():  # 首先读取sections
    print(f"section is [{section}]")
    for key in config[section]:  # 讲到每个section的键和值
        print(f"key is [{key}], value is [{config[section][key]}]")  # 打印键和值
