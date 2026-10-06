class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = digits.copy()
        i = len(digits) - 1
        while True and i >= 0:
            res[i] += 1
            if res[i] == 10:
                res[i] = 0
                i -= 1
            else:
                return res
        res.insert(0,1)
        return res   