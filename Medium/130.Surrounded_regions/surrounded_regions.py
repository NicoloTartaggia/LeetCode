class Solution:    
    def solve(self, b: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(b)==0:
            return None
        
        m, n=len(b), len(b[0])
        
        def dfs(b,i,j):
            if i<0 or j<0 or i>=len(b) or j>=len(b[0]) or b[i][j]!='O':
                return
            b[i][j]='$'   
            dfs(b,i+1,j)
            dfs(b,i-1,j)
            dfs(b,i,j+1)
            dfs(b,i,j-1)
        
        # dfs turns all "O" on the borders and all those ones connected to them to "$"
        # this logic assures us that all "O" left are surrounded by "X", so they can be transformed
        for i in range(m):  
            for j in range(n):
                if i==0 or i==m-1:
                    dfs(b,i,j)
                        
                if j==0 or j==n-1:
                    dfs(b,i,j)
                    
        
        for i in range(m):   
            for j in range(n):
                if b[i][j]=='O':
                    b[i][j]='X'
        
 
        for i in range(m):
            for j in range(n):
                if b[i][j]=='$':
                    b[i][j]='O'
                        
            