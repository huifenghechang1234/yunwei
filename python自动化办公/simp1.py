"""
title = ''
author = 'huifenghechang'
mtime = '2024/4/22'
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
自动图像下载器
"""

# Importing the necessary module and function
from simple_image_download import simple_image_download as simp

# Creating a response object
response = simp.simple_image_download

## Keyword
keyword = "Dog"

# Downloading images
try:
    response().download(keyword, 20)
    print("Images downloaded successfully.")
except Exception as e:
    print("An error occurred:", e)

