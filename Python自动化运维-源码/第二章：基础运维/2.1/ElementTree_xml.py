# -*- encoding: utf-8 -*-
import xml.etree.ElementTree as ET

tree = ET.parse("example.xml")
root = tree.getroot()
print(f"这是一个早餐菜单\n{root.attrib['year']}")

for child in root:
    print("name:", child[0].text)
    print("price:", child[1].text)
    print("description:", child[2].text)
    print("calories:", child[3].text)
