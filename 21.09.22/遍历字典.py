dict1 = {"name": "Tom", "age": "20", "gender": "male"}
for d in dict1.keys():
    print(d)
print("====================")
for value in dict1.values():
    print(value)
print("====================")
for item in dict1.items():
    print(item)
print("====================")
for key, value in dict1.items():
    print(f"{key} = {value}")