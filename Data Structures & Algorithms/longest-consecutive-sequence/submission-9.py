class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:   
        if not nums:
            return 0
        max_seq = 100000
        largest_sequence = []
        sequence = []
        seen = set()
        for num in nums:
            if num in seen:
                continue
            else:
                seen.add(num)
                left = num - 1
                right = num + 1
                while(left in seen):
                    sequence.append(left)
                    left = left - 1
                while(right in seen):
                    sequence.append(right)
                    right = right + 1
                if len(sequence) > len(largest_sequence):
                    largest_sequence = sequence
                sequence = []
        
        return len(largest_sequence) + 1