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
为查询参数添加验证
"""
import uvicorn
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: str = Query(None, max_length=50, min_length=3)):
    results = {"items": 'Big preoject'}
    if q:
        results.update({"q": q})  # 给字典results添加一个健值对{"q": q}
    return results


if __name__ == '__main__':
    uvicorn.run(app='main9:app', host="127.0.0.1", port=8080, reload=True)


"""
添加正则表达式验证

这个特定的正则表达式检查接收到的参数值：
^: 以…开头，表示字符串fixedquery前面没有字符。
fixedquery: 匹配 fixedquery 字符串.
$: 以…结尾，表示字符串fixedquery后面不匹配任何字符.
"""
from fastapi import FastAPI, Query
import uvicorn

app = FastAPI()

@app.get("/items/")
async def read_items(
 q: str = Query(None, min_length=3, max_length=50, regex="^fixedquery$") ):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


if __name__ == '__main__':
    uvicorn.run(app='main9:app', host="127.0.0.1", port=8080, reload=True)