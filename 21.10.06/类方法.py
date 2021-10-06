class Dog(object):
    __tooth = 19

    @classmethod
    def get_tooth(cls):
        return cls.__tooth

d = Dog()
result = d.get_tooth()
print(result)