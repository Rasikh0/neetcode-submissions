class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1. Find the first number from the right that is smaller than the number after it
        i = len(nums) - 2 # Because we are comparing nums[i] with number immediately after it nums[i+1]

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 2. Find the smallest number to the right that is bigger than nums[i]
        if i >= 0:
            j = len(nums) - 1 # Because j is going to search for the number we want to swap with nums[i]

            while nums[j] <= nums[i]:
                j -= 1
            
            # 3. Swap them
            nums[i], nums[j] = nums[j], nums[i]
        
        #4. Reverse everything after i
        nums[i+1:] = reversed(nums[i+1:]) # could also do nums[i+1:] = nums[i+1:][::-1]