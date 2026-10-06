class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        test = [intervals[0]]
        for start, end in intervals[1:]:
            if start < test[-1][1]:
                res += 1
                test[-1][1] = min(end, test[-1][1])
            else:
                test.append([start,end])
        return res