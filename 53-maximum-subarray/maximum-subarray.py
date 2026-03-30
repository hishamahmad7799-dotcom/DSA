class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = float('-inf')
        current = 0 
        for num in nums:
            current += num 
            if  current > max:
                max = current  
            if current < 0:
                current = 0 
                    
        return  max         
