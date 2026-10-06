class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin = 0
        leftMax = 0
        for c in s:
            if c == ")":
                leftMin = max(leftMin-1, 0)
                leftMax -= 1
            elif c == "(":
                leftMin += 1
                leftMax += 1
            else:
                leftMin = max(leftMin-1, 0)
                leftMax += 1

            if leftMax < 0:
                return False
            
        
        return min(leftMin, leftMax) == 0