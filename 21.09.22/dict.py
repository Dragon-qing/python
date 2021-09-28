dict1 = {"name": "Tom", "age": "20", "gender": "male"}
print(dict1)

dict2 = {}
dict3 = dict()
print(f"{type(dict2)}+{type(dict3)}")
print(dict1["name"])
dict1["id"] = 1001
print(dict1)

del (dict1["id"])
print(dict1)

print(dict1.items())
