from math import *

#Solution using the getting the lastdigit
n = 65433
num = n

count = 0
while num > 0:
    lastdigit = num % 10
    num = num // 10
    count = count + 1

print(count)

#Solution using log10 function
number = 6534267
counts = int(log10(number)+1)
print(counts)