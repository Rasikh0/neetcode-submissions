class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer Moore algorithm, O(1) solution
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res