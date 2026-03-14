class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # brute force approach  
        # get the size of array  
        maxSum = nums[0] 
        curSum = 0 
        for num in nums:
            curSum  += num 
            if curSum > maxSum:
                maxSum = curSum 
            if curSum < 0:
                curSum = 0    
        return maxSum        
        





            
        