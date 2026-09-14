class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #to solve this problem , we need to construct two hashmaps in which we'll store the frequencies of each character, then the solution will be the result of the comparison of those two hashmap

        s_map = {}
        t_map = {}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] not in s_map:
                s_map[s[i]] = 1
            if t[i] not in t_map:
                t_map[t[i]] = 1

            s_map[s[i]] += 1 
            t_map[t[i]] += 1
        return s_map==t_map
        

            
            


