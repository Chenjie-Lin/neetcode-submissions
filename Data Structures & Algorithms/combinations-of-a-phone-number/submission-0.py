class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numToLetter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        if not digits:
            return res
        curr = ""
        def dfs(i, curr):
            if i >= len(digits):
                res.append(curr)
                return
            for j in numToLetter[digits[i]]:
                dfs(i+1, curr + j)

            
            
        dfs(0, curr)
        return res