class Solution:
    def exist(self, b, word):
        m = len(b)
        n = len(b[0])
        visited  = set()
        res = False
    
        def dfs(i,j,visited,word,index):
            if index == len(word):
                return True
            if i<0 or i>m-1 or j<0 or j>n-1 or (i,j) in visited or word[index] != b[i][j]:
                return False
            visited.add((i,j))
    
            res = (dfs(i+1,j,visited,word,index+1) or 
            dfs(i,j+1,visited,word,index+1) or
            dfs(i-1,j,visited,word,index+1) or
            dfs(i,j-1,visited,word,index+1))

            visited.remove((i,j))
            return res
    
        for i in range(m):
            for j in range(n):
                if b[i][j] == word[0]:
                    if dfs(i,j,visited,word,0):
                        return True
                    
        return False
                
                
                    
        