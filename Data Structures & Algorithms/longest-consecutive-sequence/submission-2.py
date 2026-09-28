class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0
        nums = set(nums)
        temp = []
        for i in nums:
            if i - 1 not in nums:
                temp.append(i)
        
        for i in temp:
            j = 1
            while i + 1 in nums:
                i += 1
                j += 1
            max_len = max(max_len, j)
        return max_len



        

            