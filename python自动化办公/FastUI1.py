"""
title = ''
author = 'huifenghechang'
mtime = '2024/4/22'
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
 FastUI是一种全新的构建Web应用程序用户界面的方式，它是由声明式的Python代码定义的。它旨在为Python开发人员和前端开发人员提供一种简单而强大的工具，以便他们能够更高效地构建响应式的Web应用程序界面，而无需处理繁杂的JavaScript代码或底层的技术细节

FastUI的优势
• 对于Python开发人员，FastUI提供了使用React构建响应式Web应用程序的能力，无需编写JavaScript代码或处理npm等工具的复杂性。这使得Python开发人员可以在使用熟悉的Python语言的同时，构建出功能强大的Web应用。
• 对于前端开发人员，FastUI让他们能够专注于构建可重用的组件，而不是为每个视图都复制粘贴组件。这使得前端开发人员可以更加专注于提供用户体验和界面的创新和改进。
• 对于所有人来说，FastUI实现了后端与前端的真正分离，后端负责定义整个应用程序的逻辑，而前端则完全自由地实现用户界面

FastUI由以下四个部分组成：
• fastui PyPI包：该包提供了用于UI组件的Pydantic模型和一些实用程序。它与FastAPI配合使用效果很好，但并不依赖于FastAPI，大部分功能都可以与任何Python Web框架一起使用。
• @pydantic/fastui npm包：这是一个React TypeScript包，允许开发者在实现自己的组件时重用FastUI的机制和类型。
• @pydantic/fastui-bootstrap npm包：这是使用Bootstrap实现/定制所有FastUI组件的包。
• @pydantic/fastui-prebuilt npm包：这个包在jsdelivr.com CDN上提供了FastUI React应用程序的预构建版本，从而使开发者可以在不安装任何npm包或构建任何内容的情况下使用它。同时，Python包还提供了一个简单的HTML页面来提供此应用程序
"""

from datetime import date
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastui import FastUI, AnyComponent, prebuilt_html, components as c
from fastui.components.display import DisplayMode, DisplayLookup
from fastui.events import GoToEvent, BackEvent
from pydantic import BaseModel, Field

# 创建FastAPI应用
app = FastAPI()

# 定义用户数据模型
class User(BaseModel):
    id: int
    name: str
    dob: date = Field(title='出生日期')

# 定义一些用户
users = [
    User(id=1, name='John', dob=date(1990, 1, 1)),
    User(id=2, name='Jack', dob=date(1991, 1, 1)),
    User(id=3, name='Jill', dob=date(1992, 1, 1)),
    User(id=4, name='Jane', dob=date(1993, 1, 1)),
]

@app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
def users_table() -> list[AnyComponent]:
    """
    显示四位用户的表格，'/api' 是前端连接获取组件渲染的端点，当用户访问'/'时使用。
    """
    return [
        c.Page(
            components=[
                c.Heading(text='用户', level=2),
                c.Table(
                    data=users,
                    columns=[
                        DisplayLookup(field='name', on_click=GoToEvent(url='/user/{id}/')),
                        DisplayLookup(field='dob', mode=DisplayMode.date),
                    ],
                ),
            ]
        ),
    ]
