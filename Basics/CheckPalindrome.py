n = 14341
num = n
result = 0
while num > 0:
    lastdigit = num % 10
    result = result * 10 + lastdigit
    num = num // 10

if n == result:
    print("Palindrome")

else:
    print("Not Palindrome")