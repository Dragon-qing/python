class Dog(object):
    def work(self):
        pass


class DrugDog(Dog):
    def work(self):
        print("追踪毒品")


class ArmyDog(Dog):
    def work(self):
        print("追踪武器")


class Person(object):
    @staticmethod
    def work_with_dog(obj):
        obj.work()


if __name__ == "__main__":
    p = Person()
    dog1 = DrugDog()
    dog2 = ArmyDog()
    p.work_with_dog(dog1)
    p.work_with_dog(dog2)