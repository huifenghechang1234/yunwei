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
使用FastAPI框架来创建一个带有OAuth2密码流认证保护的Web API端点
定义了一个GET请求的/items/路由，该路由依赖于一个OAuth2密码承载令牌（token）进行访问控制

OAuth2PasswordBearer: OAuth2PasswordBearer是从fastapi.security模块导入的，它用于
创建一个OAuth2的密码流承载方案。这个方案要求客户端在请求中提供一个有效的令牌来访问受保护的资源。

tokenUrl: 这个URL是客户端用来获取访问令牌的端点。

read_items函数: 这是一个异步函数，它定义了/items/路由的处理逻辑。函数接受一个名为token的参
数，其默认值是通过Depends依赖项注入的OAuth2令牌。当客户端请求/items/时，FastAPI会检查请
求头中是否包含有效的令牌。

返回结果: 如果请求包含有效的令牌，函数将返回一个包含token的字典。请注意，出于安全原因，通常不
会直接返回令牌给客户端。这里可能是为了演示目的而这样做的
"""
import uvicorn
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}


if __name__ == '__main__':
    uvicorn.run(app='security_demo:app', host="127.0.0.1", port=8080, reload=True)
