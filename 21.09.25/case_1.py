def print_line():
    print("_" * 20, end="")


def print_lines(num):
    i = 0
    while i < num:
        print_line()
        print("X%d" % (i+1))
        i += 1


print_lines(10)