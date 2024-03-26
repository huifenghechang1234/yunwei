# encoding=utf-8

from wxpy import *

# cache_path = True 表示开启缓存功能，短时间不用重新扫码
bot = Bot(cache_path=True)

# 机器人账号自身
myself = bot.self

# 在 Web 微信中把自己加为好友
bot.self.add()
bot.self.accept()

# 发送消息给自己
bot.self.send("能收到吗？")

# 向文件传输助手发送消息
bot.file_helper.send("你好文件助手")

# 启用 puid 属性，并指定 puid 所需的映射数据保存/载入路径 puid 可始终被获取到，且具有稳定的唯一性
bot.enable_puid("wxpy_puid.pkl")

# 通过名称查找一个好友
my_friend = bot.friends().search("123")[0]
# 查看他的 puid
print(my_friend.puid)
# '26b1cc8a'
# 通过puid 来查找好友
my_friend = bot.friends().search(puid="26b1cc8a")[0]
# 向好友发送消息
my_friend.send("你好，朋友")
# 发送图片
my_friend.send_image("my_picture.png")
# 发送视频
my_friend.send_video("my_video.mov")
# 发送文件
my_friend.send_file("my_file.zip")
# 以动态的方式发送图片
my_friend.send("@img@my_picture.png")

# 查找一个群 并发送消息
## 一些不活跃的群可能无法被获取到，可通过在群内发言，或修改群名称的方式来激活
my_group = bot.groups().search("三人行")[0]
my_group.send("大家好")
# 搜索名称包含 '三人行'，且成员中包含 `my_friend` 的群聊对象
my_groups = bot.groups().search("三人行", [my_friend])
