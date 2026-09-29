class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def withinHours(k):
            total = 0
            for i in piles:
                total += -(-i // k)
            return total <= h

        lo, hi = 1, max(piles)

        while lo <= hi:
            mid = (lo + hi) // 2
            if withinHours(mid):
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1
        
        return res

