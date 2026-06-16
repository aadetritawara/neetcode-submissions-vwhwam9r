class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # helper function to check for duplicates
        def contains_duplicate(row: List[str]) -> bool:
            seen = set()
            for i in row:
                if i in seen and i != ".":
                    return True
                seen.add(i)
            return False

        # check if row is valid
        for i in range(0, 9):
            if contains_duplicate(board[i]) == True:
                return False
            
        # check if column is valid
        for i in range(0, 9):
            col = [board[j][i] for j in range(0, 9)]
            if contains_duplicate(col) == True:
                return False

        # check if sub box is valid
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_box = [board[r][c] for r in range(i, i+3) for c in range(j, j+3)]
                if contains_duplicate(sub_box) == True:
                    return False

        return True