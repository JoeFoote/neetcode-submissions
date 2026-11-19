class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while(n not in seen):
            seen.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True
        
        return False

    def sumOfSquares(self, n: int) -> int:
        output = 0
        while n:
            d = n % 10
            d = d ** 2
            output += d
            n = n // 10
        return output