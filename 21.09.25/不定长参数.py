def user_info(*args):
    print(args)


def user_info(**kwargs):
    print(kwargs)


# user_info(1, 2, 3, 4)
user_info(name="Tom", age=19, id=10)
