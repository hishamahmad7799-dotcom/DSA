class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # opposite two pointer apprpach  
        i = 0 # starrting   pointer 
        j = len(height)-1 # end pointer 
        max_water = 0 
        
        while i <j:
            h = min(height[i],height[j])
            w = j - i
            area = h * w 
            max_water = max(max_water,area)

            # move the smaller pointer 
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_water            


        