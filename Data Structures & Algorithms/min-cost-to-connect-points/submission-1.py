class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        distances = defaultdict(list)


        for i in range(len(points)):

            for j in range(i+1, len(points)):

                if i != j:

                    p1, p2 = points[i], points[j]
                    distance = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                    distances[i].append([distance, j])
                    distances[j].append([distance, i])
         
        res = 0
        visit = set()
        minHeap = [[0,0]]
        while(len(visit) < len(points)):
            cost, i = heapq.heappop(minHeap)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for ncost, nei in distances[i]:
                if nei not in visit:
                    heapq.heappush(minHeap, [ncost, nei])
        
        return res




        
