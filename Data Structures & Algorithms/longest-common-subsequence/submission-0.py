class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1) + 1
        cols = len(text2) + 1

        # Part 1: a grid of zeros (row 0 and column 0 stay 0: empty word)
        lcs = [[0] * cols for _ in range(rows)]

        # Part 2: fill in every other box, row by row
        for i in range(1, rows):
            for j in range(1, cols):
                if text1[i - 1] == text2[j - 1]:
                    lcs[i][j] = lcs[i - 1][j - 1] + 1
                else:
                    lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

        # Part 3: the bottom-right box uses all of both words
        return lcs[len(text1)][len(text2)]