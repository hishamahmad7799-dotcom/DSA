class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # kadannes algo  
        maxSum = nums[0] 
        currSum  = 0 
        for num in nums:
            currSum += num
            if currSum > maxSum:
                maxSum = currSum
            # the main logic why we are using  this algo 
            if currSum < 0:
                currSum = 0 
        return  maxSum 

       
        





            
        