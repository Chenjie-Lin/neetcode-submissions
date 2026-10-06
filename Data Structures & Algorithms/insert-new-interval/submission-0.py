class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i, i2 in enumerate(intervals):

            if  newInterval[1] < i2[0]:
                res.append(newInterval)
                return res + intervals[i:]

            elif newInterval[0] > i2[1]:
                res.append(i2)

            else:
                
                newInterval = [min(newInterval[0], i2[0]), max(newInterval[1],i2[1])]
            

        res.append(newInterval)
        
        return res
        


