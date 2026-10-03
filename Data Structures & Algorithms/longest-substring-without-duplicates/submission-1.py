class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniques = set()
        l = 0
        r = 0

        res  = 0
        while r < len(s):
            if s[r] not in uniques:
                uniques.add(s[r])
                r += 1
                res = max(res, r-l)
            else:
                uniques.remove(s[l])
                l += 1



        return res
        
        
            


        



        