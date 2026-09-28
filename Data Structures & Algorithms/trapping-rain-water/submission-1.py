class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = []
        right_max = []
        water = 0
        for i in range(len(height)):
            if i == 0:
                left_max.append(height[i])
                right_max.append(height[-i - 1])
            else:
                left_max.append(max(height[i], left_max[i-1]))
                right_max.append(max(height[-i -1], right_max[i-1]))
        for i in range(len(height)):
            water += min(left_max[i], right_max[-i - 1]) - height[i]
        return water