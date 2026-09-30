"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i : i.start)
        i = 0
        j = i + 1

        while j < len(intervals):
            t1 = intervals[j].start
            t2 = intervals[i].end
            if t1 < t2:
                return False

            i += 1
            j += 1

        return True