from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False
        l = 0
        r = len(s1) - 1

        s1_count = Counter(s1)
        tmp_count = Counter(s2[0:len(s1)])

        while r < len(s2):
            if tmp_count != s1_count:
                tmp_count[s2[l]] -= 1
                l+=1
                r+=1
                if r < len(s2):
                    tmp_count[s2[r]] += 1
            else:
                return True
        return False


        
