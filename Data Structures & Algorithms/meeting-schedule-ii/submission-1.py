"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        start = []
        end = []

        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        
        start.sort()
        end.sort()

        res = 0
        s = e = count = 0
        while s < len(intervals):

            while s < len(intervals) and start[s] < end[e]:
                s += 1
                count += 1
                res = max(count,res)

            e += 1

            count -=1

        return res

        