n = int(input())

# code here
total_sum = 0
if n == 0:
    print(0)
else:
    for i in range(0,n+1):
        total_sum = total_sum + i
    print(total_sum)