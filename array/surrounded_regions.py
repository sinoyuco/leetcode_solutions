class Solution:
    # BFS (NOT WORKING)
    def bfs(self, i , j, board, seen):
        if 0<=i<len(board) and 0<=j<len(board[0]) and board[i][j] == 'O' and (i,j) not in seen:
            if i == 0 or j == 0 or i == len(board)-1 or j == len(board[0])-1:
                return True
            seen.add((i,j))
            return self.bfs(i+1,j,board, seen) or self.bfs(i,j+1,board, seen) or self.bfs(i,j-1,board, seen) or self.bfs(i-1,j,board, seen)
        else:
            return False
        
        
        
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return []
        h,w = len(board), len(board[0])
        for i in range(h):
            for j in range(w):
                if i == 0 or j == 0 or i == h-1 or j == w-1:
                    continue
                if board[i][j] == 'O' and not self.bfs(i,j,board, set()):
                    board[i][j] = 'X'