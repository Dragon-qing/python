class Washer():
    def __init__(self):
        self.width = 300
        self.height = 200

    def __str__(self):
        return "width=%d,height=%d" % (self.width, self.height)

    def __del__(self):
        print("已删除对象")

    def print_info(self):
        print(f"洗衣机高度是:{self.height}")
        print(f"洗衣机宽度是:{self.width}")


washer = Washer()
washer.print_info()
print(washer)
del washer
x = 1 + 1
print(x)
