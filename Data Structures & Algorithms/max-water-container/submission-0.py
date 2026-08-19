class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        max = 0
        while l<r:
            area = abs(r-l) * min(heights[l], heights[r])
            if area > max:
                max = area
            if heights[l]<heights[r] and l< len(heights)-1:
                l+=1
            elif heights[l]>= heights[r] and r > 0:
                r-=1
        return max