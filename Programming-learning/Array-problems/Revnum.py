def arrayrev(nums):
    for i in range(len(nums)//2):
        nums[i],nums[len(nums)-i-1]= nums[len(nums)-i-1],nums[i]
    return nums


print(arrayrev([1,2,3,4,5]))