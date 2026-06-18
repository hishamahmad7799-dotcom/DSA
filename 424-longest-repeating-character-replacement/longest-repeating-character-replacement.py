class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """ 
        left = 0 
        ans = 0 
        freq = {}
        max_freq = 0 
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right],0)+1
            max_freq = max(max_freq,freq[s[right]])

            while (right - left +1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            ans = max(ans,right - left +1)
        return ans         


                   





         