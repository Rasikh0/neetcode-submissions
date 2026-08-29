class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] # returning the result in a list
        nums.sort() # sort the input array to eliminate duplicates

        for i, a in enumerate(nums): # index position and actual value of each item in a list
            if i > 0 and a == nums[i - 1]: # we don't want to reuse the same value in the same position 
                continue
            
            l, r = i + 1, len(nums) - 1 #use two pointers l and r to solve for two sum       
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    #update the pointers
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res