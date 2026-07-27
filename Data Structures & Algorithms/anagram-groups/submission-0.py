class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_hash = {}
        for s in strs:
            count = [0]*26
            for s_char in s:
                pos = ord(s_char)-ord('a')
                count[pos] += 1
            
            count_key = tuple(count)
            if count_key not in group_hash:
                group_hash[count_key] = []
            group_hash[count_key].append(s)
        return list(group_hash.values())  
