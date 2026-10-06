class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def withinHours(k):
            total = 0
            for i in piles:
                total += math.ceil(i / k)
            
            return total <= h

        lo, hi = 1, max(piles)
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if withinHours(mid):
                hi = mid - 1
                res = mid
            else:
                lo = mid + 1

        return res

