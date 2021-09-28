i, j = 1, 1
while i < 10:
    j = 1
    while j <= i:
        print(f"{i}X{j}={i * j}", end="\t")
        j += 1
    print()
    i += 1

