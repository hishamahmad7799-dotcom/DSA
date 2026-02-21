class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        temp = [] 

        for num  in nums:
            if num != 0:
                temp.append(num) 

        zero_count = len(nums) - len(temp) 
        for i in range(len(temp)):
            nums[i] = temp[i]
        for i in range(len(temp),len(nums)):
            nums[i] = 0                




                