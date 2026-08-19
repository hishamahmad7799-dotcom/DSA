class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # optimal approach ==> set()
        seen = set() 

        for num in nums:
            if num in seen:
                return True
            seen.add(num) 
        return False          

        
            

        