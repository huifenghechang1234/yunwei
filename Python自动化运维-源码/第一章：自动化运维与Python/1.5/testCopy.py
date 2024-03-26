# encoding=utf-8
import copy
object1 = ["Will", 28, ["Python", "C#", "JavaScript"]]
# 对象复制
object2 = copy.copy(object1)
print(f"id of object1 {id(object1)}")
print(object1)
print([id(ele) for ele in object1])


print(f"id of object2 {id(object2)}")
print(object2)
print([id(ele) for ele in object2])


# 尝试改为object1 ,然后看object2的变化

object1[0] = "Wilber"
object1[2].append("CSS")
print("更改object1之后")
print(f"id of object1 {id(object1)}")
print(object1)
print([id(ele) for ele in object1])


print(f"id of object2 {id(object2)}")
print(object2)
print([id(ele) for ele in object2])
