class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMin, currMax = 1,1

        for num in nums:
            if num == 0:
                currMin, currMax = 1,1
                continue
            currMin, currMax = min(num * currMin, num * currMax, num), max(num * currMin, num * currMax, num)
            res = max(res, currMax)
        return res
