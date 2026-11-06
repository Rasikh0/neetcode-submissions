class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        result = []

        for number in nums:
            index = abs(number) - 1

            if nums[index] < 0:
                result.append(abs(number))
            else:
                nums[index] = -nums[index]
        
        return result