"""
title = ''
author = 'huifenghechang'
mtime = '2024/2/6'
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

"""
import pybullet as p
import pybullet_data
import os
# p.connect(p.DIRECT)
p.connect(p.GUI)
p.resetSimulation()
p.setGravity(0,0,-9.8)
p.setTimeStep(1./60)
p.setRealTimeSimulation(0)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# 加载模型
floor_id = p.loadURDF('plane.urdf')
box_id = p.loadURDF(fileName='cube_no_rotation.urdf',basePosition=[2,2,0],baseOrientation=p.getQuaternionFromEuler([0, 0, 0]),useFixedBase=True)
# 需要改一下自己的路径
robot_id1 = p.loadURDF(fileName='/home/xxx/urdf_and_meshes/robomaster.urdf',basePosition=[-3,2,1],baseOrientation=p.getQuaternionFromEuler([0, 0, 0]))
robot_id2 = p.loadURDF(fileName='/home/xxx/urdf_and_meshes/robomaster.urdf',basePosition=[2,-3,1],baseOrientation=p.getQuaternionFromEuler([0, 0, 0]))

numJoints = p.getNumJoints(box_id)
print("机器人关节的数量：", numJoints)

for index in range(numJoints):
    pos = p.getLinkState(box_id,index)
    print('rbox_id index is:',pos)

print("机器人关节的信息：")
for joint_index in range(numJoints):
    joint_info = p.getJointInfo(box_id, joint_index)
    # [0]关节索引：{joint_info[0]}
    # [1]关节名称：{joint_info[1]}
    # [2]关节类型：{joint_info[2]}
    # [3]此主体的位置状态变量中的第一个位置索引：{joint_info[3]}
    # [4]在这个物体的速度状态变量中的第一个速度索引：{joint_info[4]}
    # [5]保留参数：{joint_info[5]}
    # [6]关节阻尼大小：{joint_info[6]}
    # [7]关节摩擦系数：{joint_info[7]}
    # [8]滑动或旋转关节的位置下限：{joint_info[8]}
    # [9]滑动或旋转关节的位置上限：{joint_info[9]}
    # [10]关节最大力矩：{joint_info[10]}
    # [11]关节最大速度：{joint_info[11]}
    # [12]连杆名称：{joint_info[12]}
    # [13]在当前连杆坐标系中表示的移动或转动的关节轴（忽略JOINT_FIXED固定关节）：{joint_info[13]}
    # [14]在父连杆坐标系中表示的关节位置：{joint_info[14]}
    # [15]在父连杆坐标系中表示的关节姿态（四元数x、y、z、w）：{joint_info[15]}
    # [16]父连杆的索引，若是base连杆则返回-1：{joint_info[16]}

# 打印可使用关节
joints_indexes = [i for i in range(numJoints) if p.getJointInfo(box_id, i)[2] != p.JOINT_FIXED]  # 可以使用的关节索引
print([p.getJointInfo(box_id, i) for i in joints_indexes])

# 注意因为有四个关节，所以要有四个约束；否则最终还是会移动
cid1 = p.createConstraint(floor_id, -1, box_id, 0, p.JOINT_FIXED, [0, 0, 0], [2, 2, 0], [0, 0, 0])  # 添加约束
cid2 = p.createConstraint(floor_id, -1, box_id, 1, p.JOINT_FIXED, [0, 0, 0], [2, 2, 0], [0, 0, 0])  # 添加约束
cid3 = p.createConstraint(floor_id, -1, box_id, 2, p.JOINT_FIXED, [0, 0, 0], [2, 2, 0], [0, 0, 0])  # 添加约束
cid4 = p.createConstraint(floor_id, -1, box_id, 3, p.JOINT_FIXED, [0, 0, 0], [2, 2, 0], [0, 0, 0])  # 添加约束

while True:
    p.stepSimulation()
    # 验证小车装上之后，障碍物是否会移动
    p.resetBaseVelocity(objectUniqueId=robot_id1,
                        linearVelocity=[0.1, 0, 0],
                        angularVelocity=[0, 0, 0],
                        )
    p.resetBaseVelocity(objectUniqueId=robot_id2,
                        linearVelocity=[0, 0.1, 0],
                        angularVelocity=[0, 0, 0],
                        )

