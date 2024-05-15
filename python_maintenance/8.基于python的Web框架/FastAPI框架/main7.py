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
查询参数
当你使用浏览器访问http://127.0.0.1:8080/files/?num1=2&num2=3，你会得到：{"num1 + num2 = ":5}
输入http://127.0.0.1:8080/files/
"""
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/files/")
def add(num1: int=2, num2: int=8):
    return {"num1 + num2 = ": num1 + num2}


if __name__ == '__main__':
    uvicorn.run(app='main7:app', host="127.0.0.1", port=8080, reload=True)
