class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False 

        frq = {}
        for char in s:
            frq[char] = frq.get(char,0)+1

        for char in t:
            if char not in frq:
                return False
            frq[char] -= 1

            if frq[char] < 0:
                return False
        return True         



        