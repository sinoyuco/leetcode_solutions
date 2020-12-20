class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        n = 0
        for i in S:
            if i.isdigit():
                n *= int(i)
            else:
                n+=1
                
        for i in S[::-1]:
            K%=n
            if K == 0 and i.isalpha():
                return i
            
            if i.isdigit():
                n = n / int(i)
            else:
                n-=1