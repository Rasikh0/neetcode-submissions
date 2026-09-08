class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # self.s = s
        # self.t = t
        # if sorted(s) == sorted(t):
        #     return True
        # return False

        S, T = {}, {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            S[s[i]] = 1 + S.get(s[i], 0)
            T[t[i]] = 1 + T.get(t[i], 0)
        
        for c in S:
            if S[c] != T.get(c, 0):
                return False
        return True
