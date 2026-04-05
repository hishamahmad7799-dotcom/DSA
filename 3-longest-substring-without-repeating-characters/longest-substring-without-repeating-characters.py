class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxi = 0 
        for i in range(len(s)):
            seen = set()
            for j in range(i,len(s)):
                if s[j] in seen:
                    break 
                seen.add(s[j])    
                maxi = max(maxi, j-i+1)
        return maxi            
        
        


        