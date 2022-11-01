class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = 0
        while i < len(s):
            if s[i] == '#':
                if i > 0:
                    s = s[0:i-1] + s[i+1:len(s)]
                    i -= 1
                else:
                    s = s[1:len(s)]
            else:
                i += 1
          
        i = 0
        while i < len(t):
            if t[i] == '#':
                if i > 0:
                    t = t[0:i-1] + t[i+1:len(t)]
                    i -= 1
                else:
                    t = t[1:len(t)]
            else:
                i += 1
            
        return s == t