class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # hashmap  = {}
        # for i in range(len(nums)):
        #     compliment = target - nums[i]   
        #     if compliment in hashmap:
        #         return [hashmap[compliment],i]
        #     hashmap [nums[i]] = i 
        
        # pointer appproach  
        # i,j = 0,len(nums)-1
        # while i < j:
        #     s = nums[i]+nums[j]
        #     if s == target:
        #         return [i ,j]
        #     elif  s < target:
        #         i += 1
        #     else:
        #         j -= 1        
                        
        hashmap = {}
        for  i in range(len(nums)):
            compliment  = target  - nums[i]
            if compliment in hashmap:
                return  [hashmap[compliment],i]
            hashmap[nums[i]] = i        















        