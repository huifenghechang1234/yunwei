#!/usr/bin/env python
"""Django's command-line utility for administrative tasks.

创建项目方法：
# 在命令行执行以下指令，会在当前目录生成一个名为appserver的文件夹，该文件夹中包含Django框架的一系列基础文件
django-admin startproject appserver

# 切换到appserver目录下边
cd mysite
# 创建功能模块user，此处的startapp代表创建application下的一个功能模块。
python manage.py startapp user

# 运行http://127.0.0.1:8000
python manage.py runserver 8000

"""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'appserver.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


