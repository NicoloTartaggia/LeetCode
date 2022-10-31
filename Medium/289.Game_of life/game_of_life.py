class Solution:
    def gameOfLife(self, b: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(b), len(b[0])
        
        def findLivingNeighbors(i, j):
            return sum(b[x][y] & 1 for x in range(i-1, i+2) for y in range(j-1, j+2)
                    if not (x == i and y == j) and x >= 0 and y >= 0 and x < m and y < n)
        
        for i in range(m):
            for j in range(n):
                lives = findLivingNeighbors(i, j)
                if b[i][j] & 1 == 1 and lives == 2 or lives == 3:
                    # applying in place bitwise OR operator to b[i][j] and save the result in b[i][j]
                    b[i][j] |= 2
                    
        for i in range(m):
            for j in range(n):
                # bitshifting by 1 in order to get the binary values
                b[i][j] >>= 1