class Solution:
    def moveZeroes(self, nums):
        start = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[start] = nums[i]
                start += 1
        while start < len(nums):
            nums[start] = 0
            start += 1
        return nums