class Solution:
    def climbStairs(self, n: int) -> int:
        # it's basically fibonacci
        if n <= 3:
            return n
        
        res = [0]*n
        res[0], res[1], res[2]= 1, 2, 3
        
        for i in range(3, n):
            res[i] = res[i-2]+res[i-1]
        return res[n-1]