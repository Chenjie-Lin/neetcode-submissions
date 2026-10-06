class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        hand.sort()
        if n % groupSize != 0:
            return False
        
        freq = Counter(hand)    
        minHeap = []
        for x in freq:
            heapq.heappush(minHeap, x)
        
        times = n // groupSize

        for i in range(times):
            curr = minHeap[0]
            for _ in range(groupSize):
                if curr not in freq or freq[curr] == 0:
                    return False
                
                freq[curr] -= 1
                if freq[curr] == 0:
                    heapq.heappop(minHeap)
                curr += 1

        return True
                
        
