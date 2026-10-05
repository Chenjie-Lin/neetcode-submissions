class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr = nums.copy()
        arr.extend(nums)
        return arr