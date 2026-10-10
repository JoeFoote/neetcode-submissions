class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        k_freq = []
        for i in nums:
            counts[i] += 1
        
        for n in range(0,k):
            top = max(counts, key=counts.get)
            k_freq.append(top)
            del counts[top]
        
        return k_freq
           
        
