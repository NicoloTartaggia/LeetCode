class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = strs[0]
        for i in range(1, len(strs)):
            while strs[i][:len(lcp)] != lcp and lcp:
                lcp = lcp[:len(lcp)-1]
            if not lcp:
                return ""
        return lcp
            