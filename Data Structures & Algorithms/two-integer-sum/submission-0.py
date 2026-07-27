class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in hash:
                return [hash[diff], index]
            hash[num] = index
            print(hash)
        return []