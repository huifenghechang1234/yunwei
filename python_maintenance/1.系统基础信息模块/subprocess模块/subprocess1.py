"""
title = ''
author = 'huifenghechang'
mtime = '2023/12/2'
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
subprocess模块的使用
"""
import subprocess

# 执行指定的命令，等待命令执行完成后返回一个包含执行结果的CompletedProcess类的实例
print(subprocess.run(["pip", "list"]))
print("*" * 30)
# 返回结果
# Package         Version
# --------------- -------
# cycler          0.11.0
# dnspython       2.2.1
# kiwisolver      1.3.1
# matplotlib      3.3.4
# numpy           1.19.5
# Pillow          8.4.0
# pip             10.0.1
# psutil          5.9.6
# pyparsing       3.0.7
# python-dateutil 2.8.2
# scipy           1.5.4
# setuptools      39.0.1
# six             1.16.0
# tomli           1.2.3
# xlrd            2.0.1

# subprocess.check_call()案例：执行命令，返回结果和状态，正常为0 ，执行错误则抛出异常
result1 = subprocess.call(["pip", "list"])
print("*" * 30)
print("result1结果如下")
print(result1)  # 0

result2 = subprocess.call(["pip", "list1"])
print("*" * 30)
print("result2结果如下")
print(result2)  # 1

# 运行结果
# ******************************
# 0
# ERROR: unknown command "list1" - maybe you meant "list"
# ******************************
# 1

# #  subprocess.check_call()案例：执行命令，返回结果和状态，正常为0 ，执行错误则抛出异常
result3 = subprocess.check_call(["pip", "list"])
print("*" * 30)
print("result3结果如下")
print(result3)  # 0

# result4 = subprocess.check_call(["pip", "list2"])
# print("*" * 30)
# print("result4结果如下")
# print(result4)   # 抛出异常     subprocess.CalledProcessError: Command '['pip', 'list2']' returned non-zero exit status 1

# 运行结果，运行错误，抛出异常。
# ******************************
# 0
#    raise CalledProcessError(retcode, cmd)
# subprocess.CalledProcessError: Command '['pip', 'list2']' returned non-zero exit status 1.


# # subprocess.getstatusoutput()案例：接受字符串形式的命令，返回 一个元组形式的结果，
# 第一个元素是命令执行状态，第二个为执行结果
result5 = subprocess.getstatusoutput("pip --version")
print("*" * 30)
print("result5结果如下")
print(result5)

# 返回：第一个元素0， 第二个为执行结果
# (0, 'pip 21.1.3 from C:\\lib\\site-packages\\pip (python 3.9)\n')

result6 = subprocess.getstatusoutput("pip -vesi")
print("*" * 30)
print("result6结果如下")
print(result6)
# 执行失败的案例
# (2, '\nUsage:   \n  pip <command> [options]\n\nno such option: -e')



# # subprocess.getoutput()案例：接受字符串形式的命令，放回执行结果
result7 = subprocess.getoutput("pip --version")
print("*" * 30)
print("result7结果如下")
print(result7)
# 返回
# pip 21.1.3 from D:\\lib\site-packages\pip (python 3.9)


result8 = subprocess.getoutput("pip -vesi")
print("*" * 30)
print("result8结果如下")
print(result8)
# 返回
# Usage:
#   pip <command> [options]
#
# no such option: -e


# # subprocess.check_output()案例：执行命令，返回执行的结果，而不是打印
result9 = subprocess.check_output("pip --version")
print("*" * 30)
print("result9结果如下")
print(result9)
# # 返回
# # b'pip 21.1.3 from D:\\lib\\site-packages\\pip (python 3.9)\r\r\n'


result10 = subprocess.check_output("pip -vesi")
print("*" * 30)
print("result10结果如下")
print(result10)
# 返回
#     raise CalledProcessError(retcode, process.args,
# subprocess.CalledProcessError: Command 'pip -vesi' returned non-zero exit status 2.
# 抛出callledprocessserror (retcode, process.args，
# 子流程。callledprocesserror:命令'pip -vesi'返回非零退出状态


# subprocess.Popen()综合案例
# coding:utf-8
# import time
# import datetime
# import subprocess
# from analysis_video import video_duration
#
# file = r"C:\Users\videos\duck.mp4"  # 请根据实际情况填写视频路径
# video_time = video_duration(file)
# print(video_time)
# video_pid = subprocess.Popen(f'C:\Program Files\Windows Media Player\wmplayer.exe {file}')
#
#
# # poll(): 检查进程是否终止，如果终止返回 returncode，否则返回 None。
# print(f"now:{datetime.datetime.now()}. - 当前返回状态：{video_pid.poll()}")
# # now:2021-11-28 11:20:48.504796. - 当前返回状态：None
#
# # 获取当前执行子shell的程序的进程号
# print("当前执行进程号为：{}".format(video_pid.pid))
#
# sleeps = int(video_time) + 2
# print(f"根据视频时长等待:{sleeps}秒")
# time.sleep(sleeps)
#
# # kill(): 杀死子进程。发送 SIGKILL 信号到子进程。
# video_pid.kill()
# time.sleep(1)
# print(f"now:{datetime.datetime.now()}. - 当前返回状态：{video_pid.poll()}")
# # now:2021-11-28 11:21:05.520822. - 当前返回状态：1
#
# # wait()
# # 等待命令执行完成，并且返回结果状态
# print(video_pid.wait())  # 1










