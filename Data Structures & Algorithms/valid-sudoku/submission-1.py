class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # hashmap to store all previously seen values in the row, column, or sub square
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (row // 3, col // 3)

        for r in range(9):
            for c in range(9):
                # ignore empty spaces
                if board[r][c] == ".":
                    continue

                # if current value has already been seen in its row, column, or sub square, its invalid
                if ( 
                    board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r//3, c//3)]
                    ):
                    return False

                # update hashsets
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])

        return True