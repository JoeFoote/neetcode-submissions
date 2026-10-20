class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = list(s.lower())
        backward = ["." for x in range(len(forward))]
        i = 0
        while i < len(forward):
            print(f"i: {i} length: {len(forward)}")
            if forward[i].isalnum():
                backward[len(forward)-i-1] = forward[i]
            else:
                del backward[len(forward)-i-1]
                del forward[i]
                i -= 1
            i += 1
        return forward == backward