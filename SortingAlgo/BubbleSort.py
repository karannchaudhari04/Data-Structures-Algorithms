def bubble_sort(nums):
    n = len(nums)
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
                is_swap = True
    return nums



nums = [5,8,1,6,9,2,4]
print(bubble_sort(nums))
