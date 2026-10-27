def Quick_Sort(arr,low,high):
    if low < high:
        p_index = partition(arr,low,high)
        Quick_Sort(arr,low,p_index-1)
        Quick_Sort(arr,p_index+1,high)


def partition(arr,low,high):
    pivot = arr[low]
    i = low
    j = high

    while i<j:
        while arr[i] <= pivot and i <= high-1:
            i += 1
        while arr[j] > pivot and j >= low+1:
            j -= 1

        if i<j:
            arr[i],arr[j] = arr[j],arr[i]
    arr[low],arr[j] = arr[j],arr[low]
    return j


arr = [4,1,7,6,3,2,8]
low = 0
high = len(arr)-1

Quick_Sort(arr,low,high)
print(arr)