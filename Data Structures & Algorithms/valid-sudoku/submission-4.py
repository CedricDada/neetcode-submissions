class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            hash_line = {}
            for j in range(len(board)):
                if board[i][j]!=".":
                    if board[i][j] not in hash_line:
                        hash_line[board[i][j]] = j
                    else:
                        return False
        for j in range(len(board)):
            hash_column = {}
            for i in range(len(board)):
                if board[i][j]!=".":
                    if board[i][j] not in hash_column:
                        hash_column[board[i][j]] = j
                    else:
                        return False
        
        # Définissons une matrice de hashage par bloc de 3x3 

        block_size = 3
        for r_start in range(0, len(board), block_size):
            for c_start in range(0, len(board), block_size):
                hash_block = {}
                for i in range(r_start, r_start+block_size):
                    for j in range(c_start, c_start+block_size):
                        if board[i][j]!=".":
                            if board[i][j] not in hash_block:
                                hash_block[board[i][j]] = i + block_size*j
                            else:
                                return False
        return True
