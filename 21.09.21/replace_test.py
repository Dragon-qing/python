mystr = "hello world and itcast and itheima and Python"

new_str = mystr.replace("and", "he", 2)
print(f"mystr={mystr}")
print(f"new_str={new_str}")

list1 = mystr.split("and")
list2 = mystr.split("and",2)
print(list1)
print(list2)

# join()
myList = ["aa", "bb", "cc"]
new_str = "--".join(myList)
print(new_str)