class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]
        res = ""
        for j, c in enumerate(word):
            for i in strs[1:]:
                if j == len(i) or i[j] != c:
                    return res
            res += c
        return res
            