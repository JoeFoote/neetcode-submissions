class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        b_dict = {')':'(', '}':'{',']':'['}
        b_stack = []
        for b in s:
            if b in b_dict:
                if not b_stack or b_dict[b] != b_stack.pop():
                    return False
            else:
                b_stack.append(b)
                
        return not b_stack