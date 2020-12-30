class Solution:
    def checkneigh(self, i, j, board):
        h, w = len(board), len(board[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0],
                [1, 1], [1, -1], [-1, 1], [-1, -1]]
        ct = 0
        for direction in dirs:
            if 0 <= i+direction[0] < h and 0 <= j+direction[1] < w:
                if board[i+direction[0]][j+direction[1]] == 1:
                    ct += 1
        return ct

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        h, w = len(board), len(board[0])
        b = [arr[:] for arr in board]
        for i in range(h):
            for j in range(w):
                count = self.checkneigh(i, j, board)
                if board[i][j] == 1:
                    if count < 2 or count > 3:
                        b[i][j] = 0
                else:
                    if count == 3:
                        b[i][j] = 1

        board.extend(b)
        for i in range(h):
            del board[0]
        return board
