class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        temp = []

        for num in nums:
            if num != 0:
                temp.append(num)
        count_zero = len(nums) - len(temp)
        temp.extend([0]*count_zero)           
        for i in range(len(nums)):
            nums[i] = temp[i]
        return nums            

             

                
            
         
        
        
         


                     

        



          



                