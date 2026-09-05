class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        i = 0

        while i < len(nums):
            n = nums[i]

            diff = target - n

            if diff in prevMap:
                return [prevMap[diff], i]

            prevMap[nums[i]] = i
            i += 1