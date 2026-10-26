class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        run = min(len(s), k)
        freq = {}
        l= 0
        maxf = 0
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            maxf = max(maxf, freq[s[r]])

            while (r - l + 1) - maxf > k:
                freq[s[l]] -= 1
                l += 1
            run = max(run, r-l+1)
        return run
