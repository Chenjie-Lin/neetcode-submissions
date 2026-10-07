class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def square(n):
            digit_array = [int(digit) for digit in str(n)]
            total = 0
            for i in digit_array:
                total += i ** 2
            
            return total
        
        while n not in seen:
            seen.add(n)
            n = square(n)
            if n == 1:
                return True
        
        return False
        
        
