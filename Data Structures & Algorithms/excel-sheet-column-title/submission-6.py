class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = ""
        while(columnNumber):
            columnNumber -= 1
            d = columnNumber % 26
            columnNumber //= 26
            print(d, columnNumber)
            s = chr(d+65) + s
        return s