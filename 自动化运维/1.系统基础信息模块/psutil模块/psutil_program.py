"""
title = ''
author = 'huifenghechang'
mtime = '2023/12/9'
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
import self

from yunwei1 import memory

"""
psutil模块项目应用实战
需求：长时间运行Pycharm程序，监控Pycharm程序的CPU/内存占用，以验证Pycharm程序在长时间打开的
情况下，程序是否会存在CPU占用率升高或内存泄漏的情况
"""
import psutil
import time
from turtle import pd

# 1、获取电脑整体的CPU、内存占用情况
# 获取电脑整体的CPU、内存占用情况

def getMemory(self):
    data = psutil.virtual_memory()
    memory = str(int(round(data.percent))) + "%"
    print("系统整体memory占用:"+memory)
    return memory


def getCpu(self):
    cpu_list=psutil.cpu_percent(percpu=True)
    average_cpu = round(sum(cpu_list) / len(cpu_list),2)
    cpu=str(average_cpu) + "%"
    print("系统整体cpu占用:"+cpu)
    return cpu


# 2、获取指定进程的CPU和内存占用信息代码
# 获取指定进程的CPU和内存占用信息代码
def getMemSize(pid):
        # 根据进程号来获取进程的内存大小
    process = psutil.Process(pid)
    memInfo = process.memory_info()

    # rss: 该进程实际使用物理内存（包含共享库占用的全部内存）。
    # vms：该进程使用的虚拟内存总量。

    return memInfo.rss / 1024 / 1024

def getCpuPercent(pid, self=None):
        # 根据进程号来获取进程的内存大小
    p = psutil.Process(pid)
    p_cpu = p.cpu_percent(interval=0.1)
    cpu = round(p_cpu,2)
    return cpu

def getTotalM(processName):
        # 一个进程名对应的可能有多个进程
        # 进程号才是进程的唯一标识符，进程名不是
    totalM = 0
    for i in psutil.process_iter():
        if i.name() == processName:
            totalM += processName.getMemSize(i.pid)
    print('进程占用内存：%.2f MB' % totalM)
    finalM=round(totalM,2)
    return finalM

def getTotalCPU(processName):
        # 一个进程名对应的可能有多个进程
        # 进程号才是进程的唯一标识符，进程名不是
    totalCPU = 0
    for i in psutil.process_iter():
        if i.name() == processName:
            totalCPU += processName.getCpuPercent(i.pid)
    totalCPU_convert=round(totalCPU,2)
    finalCPU=str(totalCPU_convert)+'%'
    print("进程占用CPU："+finalCPU)
    return totalCPU_convert


# 3、将测试结果数据写入csv文件
# 将测试结果数据写入csv文件
def writeExcel(caseName,cpu,mem,pycharmcpu,pycharmmem):
    timestamp = time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time()))
    dict = {'caseName': [caseName], 'Sys_CPU': [cpu],'Sys_Memory': [mem], 'Pycharm_Cpu': [pycharmcpu],'Pycharm_Mem': [pycharmmem],'OperationTime':[timestamp]}

        # 字典中的key值即为csv中列名
    dataframe = pd.DataFrame(dict)
    dataframe['OperationTime'] = pd.to_datetime(dataframe['OperationTime'])

        # 将DataFrame存储为csv, mode='a'表示每一次都是追加内容而不是覆盖，header=False表示不写列名
    dataframe.to_csv("cpuAndMemtest.csv", date_format='%Y-%m-%d-%H:%M:%S',mode='a',index=False,header=False,encoding='GBK')


# 4、封装方法为函数，以便后续直接调用
# 封装方法为函数，以便后续直接调用
def getCpuAndMem(caseName, processName1):
    memory = caseName.getMemory()
    cpu = caseName.getCpu()
        # 获取pycharm64.exe进程占用的CPU和内存
    pycharmmem = caseName.getTotalM(processName1)
    pycharmcpu = str(caseName.getTotalCPU(processName1)) + '%'

    time.sleep(1)
    caseName.writeExcel(caseName, cpu, memory, pycharmcpu, pycharmmem)
    print("系统整体CPU占用：%s     系统整体内存占用：%s   进程_CPU占用：%s  进程内存占用：%s"%(cpu, memory,pycharmcpu, pycharmmem))
    print("===============================================================")


# if __name__ == '__main__':
#     p = Psutil1()
#     #p.getCpu()
#     #p.getMemory()
#     # p.getMemSize()
#     # p.getCpuAndMem()
#     # p.getCpuPercent()
#     # p.getTotalM()
#     # p.getTotalCPU()
#     # p.writeExcel()
#     p.getCpuAndMem("pycharm64.exe")










