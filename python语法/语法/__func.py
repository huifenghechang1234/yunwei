"""
title = ''
author = 'huifenghechang'
mtime = '2024/2/7'
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
私有属性和私有方法
"""


class Phone:
    __current_voltage = 1  # 私有属性

    def __keep_single_core(self):  # 私有方法
        print("让cpu以单核模式运行")

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5g通话开始")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5g")


phone = Phone()
phone.call_by_5g()  # 类对象可以通过调用公开方法间接调用私有属性与私有方法

# 类对象无法直接调用私有属性与私有方法
# phone.__keep_single_core()
# print(phone.__current_voltage)
# print(phone.__Phone__keep_single_core)

