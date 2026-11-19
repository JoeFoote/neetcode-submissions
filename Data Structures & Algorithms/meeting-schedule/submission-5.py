"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for i in range(len(intervals)):
            for k in range(i+1, len(intervals)):
                if intervals[i].start < intervals[k].start and intervals[i].end > intervals[k].start:
                    return False
                if intervals[i].start < intervals[k].end and intervals[i].end > intervals[k].end:
                    return False
                if intervals[i].start == intervals[k].start and intervals[i].end == intervals[k].end:
                    return False
                if intervals[i].start == intervals[k].start:
                    return False
                if intervals[i].end == intervals[k].end:
                    return False
        return True