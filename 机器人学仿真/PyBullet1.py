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
1 PyBullet是什么？
PyBullet 是一个用于机器人学、游戏开发和图形研究的开源物理仿真库。它是基于 Bullet Physics SDK，这是一个成熟的、广泛使用的开源物理引擎。
PyBullet 提供了 Python 接口，使得开发者能够利用 Bullet 强大的物理仿真能力，同时享受 Python 的易用性。

1.2 PyBullet的发展历程
Bullet Physics SDK 最初由 Erwin Coumans 在 2003 年开发，它从一个小型的开源项目发展为一个强大的、被广泛认可的物理引擎，被用于电影特效、游戏和机器人仿真。
PyBullet 作为 Bullet 的 Python 接口，随着 Python 在科学计算和机器学习领域的流行。

1.3PyBullet有哪些功能及特点
多体动力学仿真: PyBullet 能够精确模拟多体系统的动态行为，包括刚体和软体动力学。
机器人学支持: 它支持加载 URDF（统一机器人描述格式）文件，这是一种在机器人学中广泛使用的标准格式。
逆向动力学和运动规划: PyBullet 提供了逆向动力学求解器和运动规划算法，这对于机器人的路径规划至关重要。
渲染和可视化: 它包括一个简单的直接渲染器，也可以通过 VR 接口进行更高级的渲染。
强化学习环境: PyBullet 与 OpenAI Gym 兼容，为强化学习提供了标准化的环境和接口。
跨平台: 它可以在 Windows、Linux 和 macOS 上运行。

1.4PyBullet有哪些优缺点
优点:
开源: 作为一个开源工具，PyBullet 有一个庞大的社区，不断有新的改进和功能添加。
性能: 对于复杂的仿真任务，PyBullet 提供了良好的性能和实时仿真能力。
易于学习: Python 接口简化了与物理引擎的交互，使得非专家也能轻松上手。
多功能性: 可以用于研究、教育和商业项目，覆盖了从基本物理仿真到高级机器人学习的各种需求。

缺点:
文档: 尽管社区支持广泛，但某些特定功能的文档可能不够详尽，新用户可能需要一段时间来熟悉。
资源消耗: 对于非常大型或复杂的仿真，PyBullet 可能需要较多的计算资源。
渲染限制: 内置的直接渲染器功能有限，对于需要高级图形的应用，可能需要额外的渲染工具。
为什么使用它进行机器人仿真

1.5 为什么使用PyBullet进行机器人仿真
PyBullet 提供了高质量的物理仿真，包括对刚体动力学、软体、碰撞检测和摩擦等物理现象的精确模拟。并且内置有逆向动力学求解器和运动规划算法。
最重要的是：PyBullet 兼容 OpenAI Gym 接口，提供了一个标准化的环境用于开发和测试强化学习算法。
"""

# 仿真一个物理世界，并在世界中放置两个球体，模拟两个球体碰撞

import pybullet as p
import pybullet_data
import time
# 启动仿真引擎的GUI
p.connect(p.GUI)
# 设置重力加速度
p.setGravity(0, 0, -9.81)
# 加载URDF模型路径
p.setAdditionalSearchPath(pybullet_data.getDataPath())
# 加载平面模型作为地面
planeId = p.loadURDF("D:\\OneDrive\桌面\\软件测试学习笔记\\多测师（西安）--测试学习集\\pythonProject1\\Lib\\site-packages\\pybullet_data\\plane.urdf")
# 加载第一个球体模型，并设置初始位置
ball1StartPos = [0, 0, 1]
ball1StartOrientation = p.getQuaternionFromEuler([0, 0, 0])
ball1Id = p.loadURDF("sphere2.urdf", ball1StartPos, ball1StartOrientation)
# 加载第二个球体模型，并设置初始位置稍微偏离第一个球体
ball2StartPos = [0.1, 0, 1]  # 稍微偏离第一个球体的位置
ball2StartOrientation = p.getQuaternionFromEuler([0, 0, 0])
ball2Id = p.loadURDF("sphere2.urdf", ball2StartPos, ball2StartOrientation)
# 设置模拟循环和时间步长
timeStep = 1./240.
p.setTimeStep(timeStep)
# 模拟循环，持续一定时间
for i in range(1000):
    p.stepSimulation()
    time.sleep(timeStep)
# 断开与仿真引擎的连接
p.disconnect()



