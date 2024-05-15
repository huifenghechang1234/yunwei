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

输入http://127.0.0.1:8080/files/home/johndoe/myfile.txt
"""

from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/files/{file_path:path}")  # 参数的名字是 file_path，:path说明参数file_path对应的类型是 path 类型
def read_user_me(file_path):
    return {"file_path": file_path}


if __name__ == '__main__':
    uvicorn.run(app='main5:app', host="127.0.0.1", port=8080, reload=True)
