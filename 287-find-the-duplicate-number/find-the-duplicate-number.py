class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # cyclic approach  
        i = 0 
        n = len(nums)
        while i < n:
            if nums[i] != i+1:
                correct  = nums[i] - 1

                if nums[i] != nums[correct]:
                    nums[i] ,nums[correct] = nums[correct],nums[i]
                else:
                    return  nums[i]
            else:
                i += 1             


             


        