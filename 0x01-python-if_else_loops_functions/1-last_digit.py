#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number % -10 if number < 0 else number % 10
print(f"Last digit of {number} is {digit} and is ", end="")
if digit > 5:
    print(f"greater than 5")
elif (digit) == 0:
    print(f"0")
else:
    print(f"less than 6 and not 0")
