class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = defaultdict(int)
        for i in tasks:
            freq[i] += 1
        
        t = 0
        maxHeap = [cnt for cnt in freq.values()]
        heapq.heapify_max(maxHeap)
        q = deque()
        while maxHeap or q:
            while q and q[0][1] < t:
                y = q.popleft()
                heapq.heappush_max(maxHeap, y[0])
                
            if maxHeap:
                x = heapq.heappop_max(maxHeap) 
                if x - 1 > 0:
                    q.append((x - 1, t + n))
            t += 1


        return t