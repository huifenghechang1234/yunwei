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
路径参数的值是路径类型变量

声明值是路径的路径参数方法：
/files/{file_path:path}
参数的名字是 file_path，:path说明参数file_path对应的类型是 path 类型

输入http://127.0.0.1:8080/files/ff/hh
"""
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/files/{file_path:path}")
def read_user_me(file_path):
    return {"file_path": file_path}


if __name__ == '__main__':
    uvicorn.run(app='main6:app', host="127.0.0.1", port=8080, reload=True)
