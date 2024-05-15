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
Cookie Parameters(Cookie参数)
定义Cookie参数，就和你定义Query和Path参数一样的方式

第一步、导入 Cookie:
from fastapi import Cookie, FastAPI 

第二步、声明Cookie参数
第一个值是默认值，您可以传递所有其他验证或注释参数：
 ads_id: str = Cookie(None)
"""
import uvicorn
from fastapi import Cookie, FastAPI

app = FastAPI()

@app.get("/items/")
async def read_items(*,
    ads_id: str = Cookie(None)
):
    return {"ads_id": ads_id}


if __name__ == '__main__':
    uvicorn.run(app='main23:app', host="127.0.0.1", port=8080, reload=True)