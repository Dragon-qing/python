class Dog(object):
    @staticmethod
    def work():
        print("hehe")


if __name__ == "__main__":
    d = Dog()
    d.work()
    Dog.work()