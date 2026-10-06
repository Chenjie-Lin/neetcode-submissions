class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        index = {}
        for i,c in enumerate(s):
            index[c] = i
        size = end = 0
        res = []
        for i in range(len(s)):
            end = max(end, index[s[i]])
            size += 1
            if i >= end:
                res.append(size)
                size = 0
        return res
        