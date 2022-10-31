class Solution:
    def bin2int(self, s: str) -> int:
        res, exp = 0, 0
        for i in range(len(s)-1, -1, -1):
            res += int(s[i]) * 2**exp
            exp += 1
        return res
    
    def int2bin(self, i: int) -> str:
        if i == 0:
            return "0"
        res = ""
        while i != 0:
            res = str(i % 2) + res
            i //= 2
        return res
    
    def addBinary(self, a: str, b: str) -> str:
        return self.int2bin(self.bin2int(a) + self.bin2int(b))