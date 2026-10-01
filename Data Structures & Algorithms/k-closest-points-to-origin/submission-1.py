class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        new_points = []
        res = []
        for i, x in enumerate(points):
            distance = math.sqrt(x[0]**2 + x[1] ** 2)
            new_points.append((distance,i))
        
        heapq.heapify_max(new_points)
        while len(new_points) > k:
            heapq.heappop_max(new_points)
        
        for x in new_points:
            res.append(points[x[1]])
        return res