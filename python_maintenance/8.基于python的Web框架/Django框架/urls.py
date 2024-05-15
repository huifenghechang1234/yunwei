"""
title = ''
author = 'huifenghechang'
mtime = '2024/3/31'
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
设置urls路径，进入到urls.py文件中，url为Django1.0版本使用，Django2.0以上版本用path
"""

from django.contrib import admin
from DjangoApp import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path(r'^index/$', views.index)
]