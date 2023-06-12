def multiply(x, y):
    try:
        x = float(x)
        y = float(y)
        return x * y
    except ValueError:
        return "Input must be number"

assert multiply(2, 3) == 6
assert multiply("0", 5) == 0
assert multiply(-4, "8") == -32
assert multiply("10", "-2") == -20
assert multiply(7.5, "2") == 15.0
assert multiply("2.5", 0.5) == 1.25
assert multiply("Hello", 5) == "Input must be number"

print("All unit tests pass")

"""
Answer:
●	What is wrong with the code?
    The code use looping for basic arithmetic operation. The function is aim to calculate the multiplication between two parameters, x and y. It can be reduce to single line
●	Which input values would you use to do the testing? positive and negative number, float and integer
●	What else worries you as you fix this problem? if the input is a string
"""