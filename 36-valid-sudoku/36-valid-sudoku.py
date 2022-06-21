class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        d_c = [{} for _ in range(9)]
        global d_3x3
        for i in range(9):
            if i%3 == 0:
                d_3x3 = [{} for _ in range(3)]
            d_r = {}
            for j in range(9):
                if board[i][j] != '.':
                    k = int(board[i][j])
                    if k not in d_r: # row check
                        d_r[k] = 0
                    else:
                        return False
                    
                    # check columns
                    if k not in d_c[j]:
                        d_c[j][k] = 0
                    else:
                        return False
                    
                    if j//3 == 0: # checking first grid
                        if k not in d_3x3[0]:
                            d_3x3[0][k] = 0
                        else:
                            return False
                    elif j//3 == 1: # checking second grid
                        if k not in d_3x3[1]:
                            d_3x3[1][k] = 0
                        else:
                            return False
                    else:           # checking third grid
                        if k not in d_3x3[2]:
                            d_3x3[2][k] = 0
                        else:
                            return False
        return True
                
                        
            