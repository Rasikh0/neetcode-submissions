class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # O(n) where n is the total number of characters given
        res = "" 

        for i in range(len(strs[0])):
            for s in strs:
                # have we reached the end of the string? (prevents us from going past the end of a string) or is the character in this string different from the character at the same position in the first string?
                if i == len(s) or s[i] != strs[0][i]: 
                    return res
            res += strs[0][i]
        
        return res
