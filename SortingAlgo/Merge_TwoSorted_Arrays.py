def merge_arrays(left,right):
    result = []
    n,m = len(left),len(right)
    i,j = 0,0

    while(i<n and j<m):
        if left[i]<=right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j+1

    if i<n:
        while i<n:
            result.append(left[i])
            i = i+1

    if j<m:
        while j<m:
            result.append(right[j])
            j = j+1

    return result


left = [1,2,3,4]
right = [1,1,3,4,5,6,7]

merge_array = merge_arrays(left,right)
# print(merge_array)