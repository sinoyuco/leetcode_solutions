class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False

        if A == B:
            return len(A) - len(set(A)) >= 1

        arr = []
        for i in range(len(A)):
            if A[i] != B[i]:
                arr.append(i)

        if len(arr) != 2:
            return False
        return A[arr[0]] == B[arr[1]] and A[arr[1]] == B[arr[0]]
