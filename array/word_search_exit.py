class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def neighbor(visited, pos, target):
            x, y = pos[0], pos[1]
            if x = 0:

            elif x == board

        for row in range(len(board)):
            for col in range(len(board[row])):
                s = word
                if board[row][col] == s[0]:
                    s = s[1:]
                    visited = [[row, col]]
                    while neighbor(visited, [row,col], s[0]):
                        #add visited cell to the visited
                        #update to the new position, trim s
                        #return true if s is empty
        return False
