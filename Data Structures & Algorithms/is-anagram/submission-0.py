class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        self.s = s
        self.t = t
        if sorted(s) == sorted(t):
            return True
        return False