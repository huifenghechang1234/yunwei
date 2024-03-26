# encoding:utf-8


import pickle

# 使用pickle模块将数据对象保存到文件

# 字符串
data0 = "hello world"
# 列表
data1 = list(range(20))[1::2]
# 元组
data2 = ("x", "y", "z")
# 字典
data3 = {"a": data0, "b": data1, "c": data2}

print(data0)
print(data1)
print(data2)
print(data3)

output = open("data.pkl", "wb")

# 使用默认的protocol
pickle.dump(data0, output)
pickle.dump(data1, output)
pickle.dump(data2, output)
pickle.dump(data3, output)
output.close()
