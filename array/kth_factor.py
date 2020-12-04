class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []

        #linear solution

        # for i in range(1, n+1):
        #     if n % i == 0:
        #         factors.append(i)
        # print(factors)
        # return -1 if k > len(factors) else factors[k-1]

        # O(logn) solution
        for i in range(1, int(sqrt(n))+1):
            if n % i == 0:
                factors.append(i)
                k -= 1
                if k == 0:
                    return i

        j = len(factors) - 1
        while j >= 0:
            if factors[j] * factors[j] == n:
                j -= 1
                continue
            elif n % factors[j] == 0:
                k -= 1
                if k == 0:
                    return n // factors[j]
            j -= 1
        return -1
