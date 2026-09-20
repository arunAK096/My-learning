class Solution:
    def missingNumber(self, nums):
        exp_sum = len(nums) * (len(nums) + 1) // 2
        act_sum = sum(nums)
        return exp_sum - act_sum