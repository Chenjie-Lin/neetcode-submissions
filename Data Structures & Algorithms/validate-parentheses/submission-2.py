class Solution:
    def isValid(self, s: str) -> bool:
        paren = {
            "}" : "{",
            "]" : "[",
            ")" : "(",
        }
        stack = []

        for i in s:
            if i not in paren:
                stack.append(i)
            elif len(stack) > 0 and stack[-1] == paren[i] :
                stack.pop()
            else:
                return False
        return len(stack) == 0
