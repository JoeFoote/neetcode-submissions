class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(32):  # check each of 32 bit positions
            if (1 << i) & n:     # build a mask for postion i AND it with n
                res += 1            # nonzero means bit i of n is 1
        return res