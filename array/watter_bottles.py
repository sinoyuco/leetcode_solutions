class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count = 0
        extras = 0
        while numBottles:
            count += numBottles
            numBottles, extras = divmod(numBottles+extras, numExchange)
        return count
