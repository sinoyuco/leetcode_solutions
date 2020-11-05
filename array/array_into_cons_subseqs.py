import collections

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        # a = [1, 2, 3, 3, 4, 4, 5, 5]
        count = collections.Counter(nums)
        #Counter({3: 2, 4: 2, 5: 2, 1: 1, 2: 1})
        tails = collections.Counter()
        #empty counter

        for x in nums:
            if count[x] == 0:
                continue
            elif tails[x] > 0:
                tails[x] -= 1
                tails[x+1] += 1
            elif count[x+1] > 0 and count[x+2] > 0:
                count[x+1] -= 1
                count[x+2] -= 1
                tails[x+3] += 1
            else:
                return False
            count[x] -= 1

        return True


        # x = 1
        # count = Counter({3: 1, 4: 2, 5: 2, 1: 0, 2: 0})
        # tails = Counter({4: 1})

        # x = 2
        # continue

        # x = 3 
        # count = Counter({3: 0, 4: 1, 5: 1, 1: 0, 2: 0})
        # tails = Counter({4: 1, 6: 1})

        #x = 3
        #continue

        #x = 4
        # count = Counter({3: 0, 4: 0, 5: 1, 1: 0, 2: 0})
        # tails = Counter({5: 1, 6: 1})

        #x = 4
        #continue

        #x = 5
        # count = Counter({3: 0, 4: 0, 5: 0, 1: 0, 2: 0})
        # tails = Counter({5: 0, 6: 2})

        #TRUE









