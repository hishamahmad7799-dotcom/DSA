class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        max_val = arr[0]
        index = 0 
        for i in range(len(arr)):
            if arr[i] > max_val:
                max_val = arr[i]
                index = i 
        return index        
        