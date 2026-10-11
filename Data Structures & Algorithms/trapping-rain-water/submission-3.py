class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0 # edge case if height = [] empty input array

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0 # stores total amount of water

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else: # when leftmax >= rightMax
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res




