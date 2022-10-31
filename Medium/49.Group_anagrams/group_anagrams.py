class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if res.get(sorted_s) == None:
                res[sorted_s] = []
            res[sorted_s].append(s)
            
        return res.values()
                