class Solution:
    def reachNumber(self, target: int) -> int:
        if target == 0:
            return 0
        if target == 1:
            return 1
        target = abs(target)
        tot = step = 0
        while True:
            if tot < target or (target-tot) % 2 == 1:
                step += 1
                tot += step
            else:
                return step
