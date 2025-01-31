# return sorted(points, key = lambda p: p[0]**2 + p[1]**2)[0:k]

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        
        for i, p in enumerate(points):
            d = p[0] * p[0] + p[1] * p[1]
            if len(maxHeap)<k:
                heappush(maxHeap, (-d, i))
            else:
                heappushpop(maxHeap, (-d,i))
        
        return [points[i] for _,i in maxHeap]
