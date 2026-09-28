class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for x in range(n):
            if x > 0 and nums[x] == nums[x-1]:
                continue
            left = x + 1
            right = n - 1
            while left < right:
                if nums[x] + nums[left] + nums[right] == 0:
                    res.append([nums[x], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left +=1
                elif nums[x] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1 
        return res