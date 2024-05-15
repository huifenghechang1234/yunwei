"""
title = ''
author = 'huifenghechang'
mtime = '2024/4/15'
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
pytest测试

使用 FastAPI 框架编写的简单应用，并使用 FastAPI 内置的 TestClient 进行测试。
这个测试用例 test_read_main 用于测试应用的 / 路径是否返回预期的 JSON 响应
"""
import uvicorn
from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

@app.get("/")
async def read_main():   # 待测试函数
    return {"msg": "Hello World"}

# 创建了一个 TestClient 对象来模拟客户端请求
client = TestClient(app)

def test_read_main():

    # 调用 client.get("/") 发送 GET 请求到应用的根路径 /，获取服务器返回的响应
    response = client.get("/")

    # 使用断言语句来验证响应的状态码和返回的 JSON 数据是否符合预期
    assert response.status_code == 200
    assert response.json() == {"msg" : "Hello World"}

if __name__ == '__main__':
    uvicorn.run(app='test_main:app', host="127.0.0.1", port=8080, reload=True)










