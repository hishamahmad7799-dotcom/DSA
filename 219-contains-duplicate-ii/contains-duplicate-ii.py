class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # brute force approach  
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             if j-i <= k:
        #                 return True
        # return False    

        # optimal approach  
        # sliding  window 
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                if i - seen[nums[i]] <=k:
                    return True 
            seen[nums[i]] = i 
        return False               
                    

        

                        

        