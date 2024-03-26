# encoding=utf-8
import configparser

config = configparser.ConfigParser()
config["DEFAULT"] = {
    "ServerAliveInterval": "45",
    "Compression": "yes",
    "CompressionLevel": "9",
}
config["bitbucket.org"] = {}
config["bitbucket.org"]["User"] = "hg"
config["topsecret.server.com"] = {}
topsecret = config["topsecret.server.com"]
topsecret["Port"] = "50022"  # mutates the parser
topsecret["ForwardX11"] = "no"  # same here
config["DEFAULT"]["ForwardX11"] = "yes"
#print(type(config["DEFAULT"].getboolean('Compression')))
#print(config["bitbucket.org"]['ServerAliveInterval'])
with open("example.ini", "w") as configfile: #将上述配置信息config写入文件example.ini
    config.write(configfile)

with open("example.ini", "r") as f: #读取example.ini 验证上述写入是否正确
    print(f.read())
