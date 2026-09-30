class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1

        for i in range(n - 1):
            old_one = one
            one = two
            two = old_one + two

        return two