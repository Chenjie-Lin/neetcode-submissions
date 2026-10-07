class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def power(x,n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            res = power(x * x, n // 2)
            return res if n % 2 == 0 else x * res
        
        num = power(x,abs(n))
        return num if n >= 0 else 1/num