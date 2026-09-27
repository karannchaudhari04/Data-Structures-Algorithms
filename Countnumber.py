n = 65433

num = n

count = 0
while num > 0:
    lastdigit = num % 10
    num = num // 10
    count = count + 1

print(count)