class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        count = 0 
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                count += 1 
        if nums[n-1] > nums[0]:
            count += 1
        return count <=1             
               
         
       