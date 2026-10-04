class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[-1] > nums[0]:
            # le tableau n'a pas subi de rotation, faisons 
            return nums[0]
        else:
            c = len(nums)//2

            # l'un des tableaux [:c] et [c:] n'a pas subi de rotations
            return min(self.findMin(nums[:c]), self.findMin(nums[c:]))
        




