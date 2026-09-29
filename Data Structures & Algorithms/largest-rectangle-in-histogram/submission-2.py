class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        stack = []
        for i, x in enumerate(heights):
            start = i
            while stack and x < stack[-1][1]:
                index, height = stack.pop()
                area = (i - index) * height
                max_area = max(area, max_area)
                start = index
            stack.append((start,x))
        
        for i, x in stack:

            area = (n-i) * x
            max_area = max(area, max_area)

        return max_area