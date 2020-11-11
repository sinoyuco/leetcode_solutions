class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        h, w = len(A), len(A[0])
        for row in range(h):
            n = []
            for col in range(w):
                n.insert(0, A[row][col])
            A.append(n)

            if row == h-1:
                for _ in range(h):
                    del A[0]
        # print(A)
        for row in range(h):
            for col in range(w):
                if A[row][col] == 0:
                    A[row][col] = 1
                else:
                    A[row][col] = 0
        return A
