class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        m = 0
        while left <= right:
            m = max((right - left) * min(heights[left], heights[right]), m)
            if heights[left] < heights[right]:
                left += 1
            else: 
                right -= 1
        return m