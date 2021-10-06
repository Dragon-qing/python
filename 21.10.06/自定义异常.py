# 自定义异常类，继承Exception
class ShortInputError(Exception):
    def __init__(self, length, min_len):
        self.length = length
        self.min_len = min_len

    def __str__(self):
        return f"你输入的长度是{self.length},不能少于{self.min_len}"

def main():
    try:
        password = input("please input password:")
        if len(password) < 3:
            raise ShortInputError(len(password), 3)
    except Exception as result:
        print(result)
    else:
        print("密码长度没有错误")

main()