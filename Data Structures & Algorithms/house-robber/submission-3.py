class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # Part 1: a street with one house
        if n == 1:
            return nums[0]

        # Part 2: make the boxes and fill in the first two by hand
        best = [0] * n
        best[0] = nums[0]
        best[1] = max(nums[0], nums[1])

        # Part 3: fill in every other box using the rule
        for i in range(2, n):
            best[i] = max(best[i - 1], nums[i] + best[i - 2])

        # Part 4: the last box is the answer for the whole street
        return best[n - 1]