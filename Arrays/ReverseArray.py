def reverseArray(nums,start,end):
    while start <= end:
        nums[start],nums[end] = nums[end],nums[start]
        start += 1
        end -= 1


nums = [10,20,30,40,50,60,70,80]
print("Original: ", nums)
reverseArray(nums,0,len(nums)-1)
print("REversed: ", nums)