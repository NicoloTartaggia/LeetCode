class Solution:
    def checkSub(self, s: str, index: int) -> bool:
        if index < len(s)-1:
            if s[index] == "I" and (s[index+1] == "V" or s[index+1] == "X"):
                return True
            if s[index] == "X" and (s[index+1] == "L" or s[index+1] == "C"):
                return True
            if s[index] == "C" and (s[index+1] == "D" or s[index+1] == "M"):
                return True
        return False
    
    def romanToInt(self, s: str) -> int:
        number = 0
        m = {"I": 1, 
             "V": 5,
             "X": 10,
             "L": 50,
             "C": 100,
             "D": 500,
             "M": 1000}

        for i in range (len(s)-1, -1, -1):
            if self.checkSub(s, i):
                number -= m[s[i]]
            else:
                number += m[s[i]]
            print(number)
        return number