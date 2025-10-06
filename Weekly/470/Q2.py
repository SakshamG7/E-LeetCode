class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        if nums.count(0) == n:
            return 0
        for i in range(len(nums)):
            prev = 0
            for j in range(i, n + i):
                prev = prev ^ nums[j]
            if prev != 0:
                return n
            else:
                n -= 1
        return 0