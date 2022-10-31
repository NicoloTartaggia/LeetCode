class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n, multiplier = 0, 1
        for i in range(len(digits)-1, -1, -1):
            n += digits[i]*multiplier
            multiplier *= 10
        
        n += 1
        
        digits = []
        while n != 0:
            digits.insert(0, n % 10)
            n //= 10
        return digits
            