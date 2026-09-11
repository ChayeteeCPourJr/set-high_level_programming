#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

last_digit = number % 10
if number < 0 and last_digit != 0:
    last_digit -= 10

if last_digit > 5:
    msg_end = "greater than 5"
elif last_digit == 0:
    msg_end = "0"
else:
    msg_end = "less than 6 and not 0"

print("Last digit of {} is {} and is {}".format(number, last_digit, msg_end))
