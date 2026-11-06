class Solution:
    def climbStairs(self, n: int) -> int:
        # Part 1: small staircases
        if n <= 2:
            return n

        # Part 2: make the boxes and fill in the first two by hand
        ways = [0] * (n + 1)
        ways[1] = 1
        ways[2] = 2

        # Part 3: fill in every other step using the rule
        for i in range(3, n + 1):
            ways[i] = ways[i - 1] + ways[i - 2]

        # Part 4: the top step is the answer
        return ways[n]