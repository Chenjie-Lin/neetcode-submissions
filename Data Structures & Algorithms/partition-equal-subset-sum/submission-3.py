class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2
        visit = {0}

        for i in nums:
            curr = visit.copy()

            for j in curr:

                if i + j == target:
                    return True

                visit.add(i+j)

        return False