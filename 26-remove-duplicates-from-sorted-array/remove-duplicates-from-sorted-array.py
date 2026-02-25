class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if not nums:
        #     return  0 
        # i = 0 
        # for j in range(1,len(nums)):
        #     if nums[j] != nums[i]:
        #         i += 1 
        #         nums[i] = nums[j] 
        # return i + 1

        # if not nums:
        #     return 0 
        # temp = []
        # temp.append(nums[0])
        # for i in range(1,len(nums)):
        #     if nums[i] != nums[i-1]:
        #         temp.append(nums[i])
        # for i in range(len(temp)):
        #     nums[i] = temp[i]
        # return len(temp) 

        if not nums:
            return 0 
        i = 0 
        for j in range(1,len(nums)):
            if nums[j] != nums[i]:
                i += 1 
                nums[i] = nums[j]
        return  i +1         
            

       

        



          
        