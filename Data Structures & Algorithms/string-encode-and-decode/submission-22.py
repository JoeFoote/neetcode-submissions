class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        if not strs:
            return s
        else:
            for string in strs:
                s = s + str(len(string)) + "#" + string
        return s

    def decode(self, s: str) -> List[str]:
        new_str = ""
        strs = []
        length = 0
        length_str = ""
        delimiter_seen = False
        for i in range(0,len(s)):
            #print(s)
            if s[i] == "#" and delimiter_seen == False:
                delimiter_seen = True
                length = int(length_str)
                if length == 0:
                    strs.append("")
                    length_str = ""
                    delimiter_seen = False
                continue
            # Build length of string before 
            if delimiter_seen == False:
                length_str = length_str + s[i]
            else:
                if length > 1:
                    new_str = new_str + s[i]
                    length -= 1
                else:
                    new_str = new_str + s[i]
                    strs.append(new_str)
                    new_str = ""
                    length_str = ""
                    length = 0
                    delimiter_seen = False
                
        return strs