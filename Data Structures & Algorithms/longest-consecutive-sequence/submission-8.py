class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:   
        if not nums:
            return 0
        h = []
        seen = set()
        for num in nums:
            if num in seen:
                continue
            else:
                seen.add(num)
                heapq.heappush(h, num)
        #print(h)
        sorted_h = [heapq.heappop(h) for i in range(len(h))]
        print(sorted_h)
        sequence = 1
        largest_sequence = 1
        last = sorted_h[0]
        for num in sorted_h:
            diff = num - last
            # skip first element
            if last == num:
                continue
            if diff != 1:
                if sequence > largest_sequence:
                    largest_sequence = sequence
                sequence = 1
            else:
                sequence += 1
            last = num
        if sequence > largest_sequence:
            return sequence
        return largest_sequence