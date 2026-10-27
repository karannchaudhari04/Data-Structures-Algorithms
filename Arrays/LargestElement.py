def largest(arr):
    n = len(arr)
    larger = arr[0]
    for i in range(0,n):
        if arr[i] > larger:
            larger = arr[i]
    return larger

arr = [-10,20,-70,40,15,7]
print(largest(arr))