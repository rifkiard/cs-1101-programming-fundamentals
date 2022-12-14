import math

# Part 1
def my_sqrt(a):
    x = a / 2
    while True:
        y = (x + a/x) / 2.0
        if y == x:
            break
        x = y 
    return y

# Part 2
def test_sqrt():
    print("a", " " * 10, 'my_sqrt(a)', ' ' * 10, 'math.sqrt(a)', ' ' * 8, "diff")
    print("-", " " * 10, '-' * 9, ' ' * 11, '-' * 11, ' ' * 9, "-" * 4)

    for a in range(1, 26):
        value_of_my_sqrt = my_sqrt(a)
        value_of_math_sqrt = math.sqrt(a)
        diff = value_of_math_sqrt - value_of_my_sqrt
        print(a, " " * (11 - len(str(a))),  value_of_my_sqrt, " " * (20 - len(str(value_of_my_sqrt))), value_of_math_sqrt, " " * (20 - len(str(value_of_math_sqrt))), diff)

test_sqrt()