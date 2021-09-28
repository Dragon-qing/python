a = 100


def function1():
    print(a)


def function2():
    global a
    a = 200
    return 1, 2, 3, 4


function1()
print(function2())
function1()


