class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return 
        
        d = defaultdict(int) 
        for i in range(len(s)):
            if not d.get((s[i]), None):
                d[s[i]] = 1
            else:
                d[s[i]] += 1
                
            if not d.get((t[i]), None):
                d[t[i]] = -1
            else:
                d[t[i]] -= 1
            
        for v in d.values():
            if v != 0:
                return False
        return True