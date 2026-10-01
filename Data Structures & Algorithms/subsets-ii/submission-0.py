class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        curr = []

        seen = set()

        def dfs(i, seen):
            if i >= len(nums):
                res.append(curr.copy())
                return

            if nums[i] in seen:
                dfs(i+1, seen.copy())

            else:

                curr.append(nums[i])
                dfs(i + 1, seen.copy())

                curr.pop()
                seen.add(nums[i])
                dfs(i + 1, seen.copy())

        dfs(0,seen)
        
        return res
            
            
        