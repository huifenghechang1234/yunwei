# -*- coding: UTF-8 -*-

arr = [1000000, 600000, 400000, 200000, 100000, 0] #定义利润列表
rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1] #定义提成比例列表，与利润列表一一对应


while True:
    i = input('净利润(q退出): ') #获取用户输入
    if i == 'q':
        exit(0)  #退出程序
    if not i.isdigit():  #如果不是数字，则重新开始循环，重新输入数据
        continue
    reward = []   #定义奖金列表，存放每一区间计算的奖金
    print("奖金为：",end='')  #不换行
    I=int(i)
    for idx in range(0, 6):
        if I > arr[idx]:
            reward.append ((I - arr[idx]) * rat[idx])   #将每一区间的奖金存放在奖金列表中
            I = arr[idx]
    reward.reverse()  #逆序奖金列表，目的为方便输出
    if(len(reward)) == 1: #如果只有一个，直接输出
        print(reward[0])
    else:
        print(" + ".join([str(num) for num in reward]),"=",sum(reward)) #输出每个区间的奖金，并求和

