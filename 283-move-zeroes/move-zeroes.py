class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #1.create a temp   list  
        temp = []

        #2.store all non zero element 
        for num in nums:
            if num != 0 :
                temp.append(num)
        #3.count zero 
        count_zeroes = len(nums) - len(temp)
        #4.add zereos at end of an array  
        temp.extend ([0]*count_zeroes)  
        #5.copy back to origina array  
        for i in range(len(nums)):
            nums[i] = temp[i]      
        
                
            
         
        
        
         


                     

        



          



                