import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = s.lower()
        l = l.replace(" ", "")
        l = re.sub(r'[^a-zA-Z0-9]', '', l)
        g = 0
        d = len(l)-1
        
        while g!=d and g<len(s)-1 and d>0:
            if(l[g] != l[d]):
                print(s)
                return False
            g += 1
            d -= 1
        return True