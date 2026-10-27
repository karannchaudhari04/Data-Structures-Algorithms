def secondlargest(arr):
    n = len(arr)
    larger = float("-inf")
    secondlargest = float("-inf")

    for i in range(0,n):
        if arr[i] > larger:
            secondlargest = larger
            larger = arr[i]

        elif arr[i] > secondlargest and arr[i] != larger:
            secondlargest = arr[i]

    return secondlargest

arr = [10,20,65,40,50,60,70]
print(secondlargest(arr))