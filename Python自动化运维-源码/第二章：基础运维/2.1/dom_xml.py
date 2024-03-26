#!/usr/bin/python3

from xml.dom.minidom import parse
import xml.dom.minidom

# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse("example.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("year"):
    print(f"这是一个早餐的菜单\n年份 {collection.getAttribute('year')}")

# 在集合中获取所有早餐菜单信息
foods = collection.getElementsByTagName("food")

# 打印每部电影的详细信息
for food in foods:
    type = food.getElementsByTagName("name")[0]
    print("name: %s" % type.childNodes[0].data)
    format = food.getElementsByTagName("price")[0]
    print("price: %s" % format.childNodes[0].data)
    rating = food.getElementsByTagName("description")[0]
    print("description: %s" % rating.childNodes[0].data)
    description = food.getElementsByTagName("calories")[0]
    print("calories: %s" % description.childNodes[0].data)
