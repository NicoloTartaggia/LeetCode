class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # we take only those paper whose citation is bigger than its index
        # [3,0,6,1,5] -> [6,5,3,1,0] -> 6 >0, 5 > 1, 3 > 2 -> sum = 3
        # [1,3,1] -> [3,1,1] -> 3 > 0 -> sum = 1
        return sum(i < j for i, j in enumerate(sorted(citations, reverse=True)))