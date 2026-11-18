class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while(len(stones) > 1):
            a = heapq.heappop_max(stones)
            b = heapq.heappop_max(stones)
            if a != b:
                diff = a - b
                heapq.heappush_max(stones, diff)
        return 0 if not stones else stones[0]