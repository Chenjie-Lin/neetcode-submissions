class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def helper(x,y):
            if len(y) > len(x):
                x, y = y, x
            
            total = 0
            pad = 1
            pad2 = 1
            res = ""
            for i in range(len(x)):
                pad2 = 1
                for j in range(len(y)):
                    total += int(x[-i - 1]) * int(y[-j - 1]) * pad * pad2
                    pad2 *= 10
                pad *= 10
            
            res = str(total)
            return res
        
        return helper(num1,num2)