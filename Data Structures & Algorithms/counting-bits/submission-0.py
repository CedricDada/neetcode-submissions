class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n+1):
            res_i = 0
            while i!=0:
                res_i += 1
                i = i & (i - 1)
            res.append(res_i)
        return res
