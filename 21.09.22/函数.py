def function(a, b):
    a += 1
    b += 2
    return a, b


number1 = 1
number2 = 2
number1, number2 = function(number1, number2)
print(number1, number2)
tuple1 = function(number1, number2)
print(tuple1)
