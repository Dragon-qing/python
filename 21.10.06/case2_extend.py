class Master(object):
    def __init__(self):
        self.kongfu = "[古法煎饼果子配方]"

    def make_cake(self):
        print(f"用{self.kongfu}制作煎饼果子")


class School(object):
    def __init__(self):
        self.kongfu = "[独创煎饼果子配方]"

    def make_cake(self):
        print(f"用{self.kongfu}制作煎饼果子")


class Prentice(School, Master):
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


class Tusun(Prentice):
    pass


if __name__ == "__main__":
    tusu = Tusun()
    tusu.make_master_cake()
    tusu.make_cake()
    tusu.make_school_cake()
