class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        b = "(" * k + ")" * k
        n = s.count(b)
        while n > 0:
            for i in range(n):
                s = s.replace(b, "")
            n = s.count(b)
        return s
