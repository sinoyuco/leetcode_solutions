import math


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        m, mi = math.inf, -1
        currg = 0
        for i in range(len(gas)):
            currg += gas[i]-cost[i]
            if currg < m:
                m = currg
                mi = i
        return (mi+1) % len(gas) if currg >= 0 else -1
