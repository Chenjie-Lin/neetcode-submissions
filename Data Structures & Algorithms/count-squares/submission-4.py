class CountSquares:

    def __init__(self):
        self.pointsCount = defaultdict(int)


    def add(self, point: List[int]) -> None:
        self.pointsCount[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.pointsCount:
            if (abs(y-py) != abs(x-px)) or x == px or y == py:
                continue
            res += (self.pointsCount.get((x,py), 0)  *    
                    self.pointsCount.get((px,y), 0) * self.pointsCount.get((x,y), 0))
            
        return res

        
