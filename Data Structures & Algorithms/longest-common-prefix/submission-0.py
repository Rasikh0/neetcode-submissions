class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # O(n) where n is the total number of characters given
        res = "" 

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        
        return res
