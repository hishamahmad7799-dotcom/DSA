class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(start,path):
            result.append(path[:])

            for i in range(start,len(nums)):
                #choose 
                path.append(nums[i])
                #explore
                backtrack(i+1,path)
                #undo 
                path.pop()
        backtrack(0,[])
        return result
                
        