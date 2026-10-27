class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        # a - z characters
        s1_arr = [0]*26
        for i in range(len(s1)):
            s1_arr[ord(s1[i])-97] += 1
        l = 0
        win_arr = [0]*26
        for r in range(len(s2)):
            win_arr[ord(s2[r])-97] += 1
            if win_arr == s1_arr:
                return True
            if r-l+1 == len(s1):
                win_arr[ord(s2[l])-97] -= 1
                l += 1
        return False

        