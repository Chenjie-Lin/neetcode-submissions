class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        suf = [1]
        p = 1
        s = 1
        for i in range(1, len(nums)):
            p *= nums[i-1]
            s *= nums[-i]
            pre.append(p)
            suf.append(s)
        suf.reverse()
        res = []
        return [a * b for a, b in zip(pre, suf)]
