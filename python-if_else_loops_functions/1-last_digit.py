#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    lstdg = number % 10
else:
    lstdg = number % -10
if (lstdg > 5):
    print("Last digit of", number, "is", lstdg, "and is greater than 5")
elif (lstdg == 0):
    print("Last digit of", number, "is", lstdg, "and is 0")
else:
    print("Last digit of", number, "is", lstdg, "and is less than 6 and not 0")
