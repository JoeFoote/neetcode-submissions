class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:   
        if not nums:
            return 0
        num_set = set(nums)
        longest = 0
    
        for num in num_set:
            left = num - 1
            if left not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                if length > longest:
                    longest = length
        return longest