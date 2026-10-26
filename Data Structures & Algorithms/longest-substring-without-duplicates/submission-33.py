class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        run = 0
        seen = {}
        l = 0
        for r in range(0, len(s)):
            if s[r] not in seen:
                seen[s[r]] = r # save index of value
            else:
                if seen[s[r]] >= l:
                    l = seen[s[r]] + 1
                seen[s[r]] = r
            
            run = max(run, (r-l+1))
        return run