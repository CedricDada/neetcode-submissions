class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m*n - 1


        new_matrix = []
        for i in range(m):
            for j in range(n):
                new_matrix.append(matrix[i][j])

        while l < r:
            if new_matrix[l] < target:
                l += 1
            elif new_matrix[l] == target:
                return True
            if new_matrix[r] > target:
                r -= 1
            elif new_matrix[r] == target:
                return True
            
        if new_matrix[l] != target:
            return False
        return True

        
