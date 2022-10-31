class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = {}
        for i in range(0, len(s)-9):
            v = s[i:i+10]
            if v in res:
                res[v] += 1
            else:
                res[v] = 1
        return [k for k,v in res.items() if v > 1]