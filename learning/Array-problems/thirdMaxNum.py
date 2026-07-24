class Solution:
   def thirdMax(self, nums):
      temp = set(nums)
      temp = sorted(temp, reverse=True)
      if len(temp) >= 3:
         return temp[2]              
      else:
            return max(temp)