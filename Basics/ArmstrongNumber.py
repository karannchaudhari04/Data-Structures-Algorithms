from math import *

num = 153
n = num
total = 0

count = len(str(num))

while n > 0:
    lastdigit = n % 10
    total = total + (lastdigit ** count)
    n = n // 10

if total == num:
    print("Armstrong Number")

else:
    print("Not Armstrong Number")

