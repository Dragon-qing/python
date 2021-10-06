class Master(object):
    def __init__(self):
        self.kongfu = "[古法煎饼果子配方]"
        self.__money = 10000

    def __print_info(self):
        print(self.kongfu, self.__money)

    def make_cake(self):
        print(f"用{self.kongfu}制作煎饼果子")
        self.__print_info()


class School(Master):
    def __init__(self):
        self.kongfu = "[独创煎饼果子配方]"

    def make_cake(self):
        print(f"用{self.kongfu}制作煎饼果子")
        super().__init__()
        super().make_cake()
        super().__init__()


class Prentice(School):
    def __init__(self):
        self.kongfu = "[综合煎饼果子配方]"

    def make_cake(self):
        self.__init__()
        print(f"用{self.kongfu}制作煎饼果子")

    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

    def make_old_cake(self):
        super().__init__()
        super().make_cake()


if __name__ == "__main__":
    pre = Prentice()
    pre.make_old_cake()
