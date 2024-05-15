"""
title = ''
author = 'huifenghechang'
mtime = '2024/4/14'
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
限定路径参数有效值
输入http://127.0.0.1:8080/hjx/jj
"""
# import uvicorn
# from enum import Enum
# from fastapi import FastAPI
#
#
# class Hjx_Class_name(str, Enum):
#     Name = 'huangjunx'
#     Year = 18
#     Id = '20153201072'
#     student = True
#
#
# app = FastAPI()
#
#
# @app.get('/hjx/{hjx_man}')
# def root(hjx_man: Hjx_Class_name):
#     return {'status': hjx_man}
#
# if __name__ == '__main__':
#     uvicorn.run(app='main2:app', host="127.0.0.1", port=8080, reload=True)




"""
无论你使用哪个类属性的值访问，结果都是{"status":"huangjunx"}
可以在root函数里面调用这个类的类属性。通过Hjx_Class_name.Name进行调用

输入http://127.0.0.1:8080/hjx/77
"""
from enum import Enum
from fastapi import FastAPI
import uvicorn

class HjxEnum(Enum):
    NAME = 'huangjunx'
    YEAR = 18
    ID = '20153201072'
    # 注意：Enum 成员通常是大写的，并且不应该包含像 "student" 这样的布尔值，因为它不是常量


app = FastAPI()


@app.get('/hjx/{hjx_member}')
def root(hjx_member: HjxEnum):
    # 这里返回了枚举成员的名称对应的值
    return {'status': hjx_member.value}

if __name__ == '__main__':
    uvicorn.run(app='main2:app', host="127.0.0.1", port=8080, reload=True)