import math

i = 0
while i < 100:
    if i == 0 or i == 1:
        i += 1
        continue
    j = 2
    while j <= math.sqrt(i):
        if i % j == 0:
            i += 1
            continue
        j += 1
    if j > math.sqrt(i):
        print(i)
    i += 1
