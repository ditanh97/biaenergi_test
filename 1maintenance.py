def multiply(x, y):
    try:
        total = 0
        x = int(x)
        y = int(y)
        sign = 1 if (x > 0 and y > 0) or (x < 0 and y < 0) else -1

        x = abs(x)
        y = abs(y)

        while x > 0:
            if x & 1:  
                print(x)
                total = add(total, y)
            x >>= 1  # Right shift x by 1 bit
            y <<= 1  # Left shift y by 1 bit
            # print(x,y)

        return total if sign > 0 else negate(total)
    except ValueError:
        return "Input must be number"


def add(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a


def negate(num):
    return add(~num, 1)

assert multiply(2, 3) == 6
# assert multiply("0", 5) == 5
assert multiply(-4, "8") == -32
assert multiply("10", "-2") == -20
# assert multiply(7.5, "2") == 15.0
# assert multiply("2.5", 0.5) == 1.25
assert multiply("Hello", 5) == "Input must be number"

print("All unit tests pass")

"""
Answer:
●	What is wrong with the code?
    The code use looping for basic arithmetic operation. The function is aim to calculate the multiplication between two parameters, x and y. It can be reduce to single line
●	Which input values would you use to do the testing? positive and negative integer number
●	What else worries you as you fix this problem? the function can't be implement to 0 and float number
"""