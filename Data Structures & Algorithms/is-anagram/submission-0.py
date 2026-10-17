class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        s_len = len(s)
        t_len = len(t)
        if (s_len != t_len):
            return False
        for i in range(0,s_len):
            if s[i] not in s_dict:
                s_dict[s[i]] = 0
            else:
                s_dict[s[i]] += 1

            if t[i] not in t_dict:
                t_dict[t[i]] = 0
            else:
                t_dict[t[i]] += 1

        if s_dict == t_dict:
            return True
        return False


        