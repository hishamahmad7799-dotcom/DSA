class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0 
        j = len(height)-1
        max_water = 0 

        while i < j:
            h = min(height[i],height[j])
            w = j - i 
            area = h*w 
            max_water = max(max_water,area)
            if  height[i] < height[j]:
                i += 1
            else:
                j -= 1    
        return  max_water        


        