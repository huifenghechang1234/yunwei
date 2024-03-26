#!/usr/bin/python3

import xml.sax


class MenuHandler(xml.sax.ContentHandler):

    def __init__(self):
        self.CurrentData = ""
        self.name = ""
        self.price = ""
        self.description = ""
        self.calories = ""

    # 元素开始调用
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "breakfast_menu":
            print("这是一个早餐的菜单")
            year = attributes["year"]
            print(f"年份 {year}\n")

    # 读取字符时调用
    def characters(self, content):
        if self.CurrentData == "name":
            self.name = content
        elif self.CurrentData == "price":
            self.price = content
        elif self.CurrentData == "description":
            # 如果有内容有换行请累加字符串，输出后清空该属性
            self.description += content
        elif self.CurrentData == "calories":
            self.calories = content
        else:
            pass

    # 元素结束调用
    def endElement(self, tag):
        if self.CurrentData == "name":
            print(f"name:{self.name}")
        elif self.CurrentData == "price":
            print(f"price:{self.price}")
        elif self.CurrentData == "description":
            print(f"description:{self.description}")
            # 内容有换行时，获取字符串后请空该属性，为下一个标签准备
            self.description = ""
        elif self.CurrentData == "calories":
            print(f"calories:{self.calories}")
        else:
            pass
        self.CurrentData = ""


if __name__ == "__main__":
    # 创建一个 XMLReader
    parser = xml.sax.make_parser()
    # 重写 ContextHandler
    Handler = MenuHandler()
    parser.setContentHandler(Handler)

    parser.parse("example.xml")
