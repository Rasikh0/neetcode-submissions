from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_val = max(nums)
        points = [0] * (max_val + 1)
        for num in nums:
            points[num] += num

        prev2, prev1 = 0, 0
        for v in range(max_val + 1):
            prev2, prev1 = prev1, max(prev1, prev2 + points[v])

        return prev1