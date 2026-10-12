class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x: x[1])
        non_overlapped = []



        for i in range(len(intervals)):
            if not non_overlapped:
                non_overlapped.append(intervals[i])
            else:
                # en cas de chevauchement , il faut suprpimer le plus large
                last_added = non_overlapped[-1]
                if intervals[i][0] >= last_added[1]: # il n'y a pas de chevauchement
                    non_overlapped.append(intervals[i])
                
                # s'il y a chevauchement on ne l'ajoute pas 
        return len(intervals) - len(non_overlapped)
            
