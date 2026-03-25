class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # cyclic sort
        i = 0 
        n = len(nums)
        while i < n:
            corr = nums[i]
            if nums[i] < n  and nums[i] != nums[corr]:
                nums[i],nums[corr] = nums[corr],nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i:
                return i   
        return n               


        