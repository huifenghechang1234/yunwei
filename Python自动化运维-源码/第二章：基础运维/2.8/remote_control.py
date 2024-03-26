import subprocess

from wxpy import *
from wechat_sender import *
bot = Bot()
#指定管理员
admin = bot.friends().search("清如")[0]


def remote_shell(command):
    r = subprocess.run(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
    )
    if r.stdout:
        yield r.stdout
    else:
        yield "[OK]"


def send_iter(receiver, iterable):
    """
   用迭代的方式发送多条消息

   :param receiver: 接收者
   :param iterable: 可迭代对象
   """

    if isinstance(iterable, str):
        raise TypeError

    for msg in iterable:
        receiver.send(msg)


@bot.register()
def server_mgmt(msg):
    """
        若消息文本以 ! 开头，则作为 shell 命令执行
    """
    print(msg)
    if msg.chat == admin:
        if msg.text.startswith("!"):
            command = msg.text[1:]
            send_iter(msg.chat, remote_shell(command))

#进入阻塞，可以在命令行调试
embed()
