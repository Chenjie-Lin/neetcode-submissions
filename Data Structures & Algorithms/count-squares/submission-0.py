class CountSquares:

    def __init__(self):
        self.pointsCount = defaultdict(int)


    def add(self, point: List[int]) -> None:
        self.pointsCount[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for (x, y), cnt in list(self.pointsCount.items()):
            if (abs(y-py) != abs(x-px)) or x == px or y == py:
                continue
            res += (self.pointsCount[(x,py)]  *    
                    self.pointsCount[(px, y)]) * self.pointsCount[(x,y)]
            
        return res

        
