class Solution:
    def removeDuplicates(self, nums):
        emp = []
        count = 0

        for i in range(len(nums)):
            if nums[i] not in emp:
                emp.append(nums[i])
                count += 1
        for i in range(len(emp)):
            nums[i] = emp[i]
        return count