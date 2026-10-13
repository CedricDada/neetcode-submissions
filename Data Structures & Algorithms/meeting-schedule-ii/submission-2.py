import heapq
# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)
        res = 0
        heap = []
        for interval in intervals:
            if not heap:
                heapq.heappush(heap, interval.end)
                res += 1
            else:
                if interval.start < heap[0]:
                    res += 1 
                    heapq.heappush(heap, interval.end)
                else: # il y a pas de chevauchement avec la salle qui s'est libéré le plus récemment, je mets mon évenement dans cette salle
                    end_time = heapq.heappop(heap)
                    heapq.heappush(heap, interval.end)
        return res
        