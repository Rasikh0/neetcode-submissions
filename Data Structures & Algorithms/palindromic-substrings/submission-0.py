class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        n = len(s)

        for i in range(n):
            left = i
            right = i

            while left >= 0 and right < n and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1

            left = i
            right = i + 1

            while left >= 0 and right < n and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1

        return result