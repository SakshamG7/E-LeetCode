def contains_zeros(n: int) -> bool:
        if n == 0:
            return True
        while n > 0:
            if n % 10 == 0:
                return True
            n //= 10
        return False
def old(n):
    l = 0
    n1 = n - 1
    n2 = 1
    for i in range(n//2):
        if not (contains_zeros(n1) or contains_zeros(n2)):
            l += 2
            if n1 == n2:
                l -= 1
        n1 -= 1
        n2 += 1
    return l

class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        if n <= 10:
            return n - 1
        l = n
        m = 10
        while m <= n:
            l -= n // m
            m *= 10
        c = 1
        while n > 0:
            if n % 10 != 0:
                l -= 1
            n //= 10
        return l

import time
# 101
# print(Solution().countNoZeroPairs_(12)) # 9
# for i in range(10, 10**15 + 1):
for i in range(10, 101 + 1):
    n1 = Solution().countNoZeroPairs(i)
    n2 = old(i)
    if n1 != n2:
        print(i, n1, n2)
        # break
    # time.sleep(1)