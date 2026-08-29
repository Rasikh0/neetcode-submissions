class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #detecting duplicates with a hashmap
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r//3, c//3)

        #iterate through the entire grid
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": #if empty skip
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False # if value already in current row, current column, or current square return false
                cols[c].add(board[r][c]) #making sure hashmaps are updated
                rows[r].add(board[r][c]) #and making sure duplicates are detected when we get to the next iteration of the loop
                squares[(r // 3, c // 3)].add(board[r][c])
        return True
