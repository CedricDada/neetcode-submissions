from heapq import heapify, heappop, heappush
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for val in nums:
            if val in freqs:
                freqs[val] += 1
            else:
                freqs[val] = 1

        heap = []
        for val, freq in freqs.items():
            heappush(heap, tuple([freq,val]))
        
            if len(heap)>k:
                heappop(heap)
        
        return [val for (freq, val) in heap]



