# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)
        prev = None
        for interval in intervals:
            print("interval : ", interval.start, interval.end)
            if not prev:
                prev = interval
            else:
                print("prev : ", prev.start, prev.end)
                if interval.start < prev.end:
                    return False
                prev = interval
        return True