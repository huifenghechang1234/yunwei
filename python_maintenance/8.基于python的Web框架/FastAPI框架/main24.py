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
Header Parameters(Header参数)
定义Header参数，就和你定义Query和Path参数一样的方式

第一步、导入 Header:
from fastapi import Cookie, FastAPI ， Header 

第二步、声明Header参数
第一个值是默认值，您可以传递所有其他验证或注释参数：
 ads_id: str = Header(None)
"""
import uvicorn
from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/items/")
async def read_items(*, user_agent: str = Header(None)):
    return {"User-Agent": user_agent}


if __name__ == '__main__':
    uvicorn.run(app='main24:app', host="127.0.0.1", port=8080, reload=True)