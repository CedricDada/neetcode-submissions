class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        parent = {}
        for i, val in enumerate(nums):
            if val not in parent:
                parent[val] = val
            if val-1 in parent:
                parent[val] = val-1
            if val+1 in parent:
                parent[val+1] = val
        visited = set()
        length = 1
        for key, val in parent.items():
            length_key = 1
            if key not in visited:
                next = key
                visited.add(next)
                while(next in parent and parent[next]!=next):
                    length_key += 1
                    next = parent[next]
                    visited.add(next)
                if length_key > length:
                    length = length_key
        return length