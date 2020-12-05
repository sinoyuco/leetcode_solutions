class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        ct = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                ct+=1
            else:
                ct = 0
            if ct == 3:
                n-=1
                ct = 1
            if n == 0:
                return True
        return False