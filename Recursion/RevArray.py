def revArray(nums,left,right):
    if left >= right:
        return
    nums[left],nums[right] = nums[right], nums[left]
    revArray(nums,left+1,right-1)

nums = [10,20,30,40,50]
revArray(nums,0,len(nums)-1)
print(nums)