class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Solution with count 
        return all(ransomNote.count(x) <= magazine.count(x)   for x in set(ransomNote))
        
        # Solution with defaultdict
        # d = defaultdict(int)
        # for i in range(len(magazine)):
        #     if not d.get((magazine[i]), None):
        #         d[magazine[i]] = 1
        #     else:
        #         d[magazine[i]] += 1
        
        # for i in range(len(ransomNote)):
        #     if not d.get((ransomNote[i]), None) or d.get((ransomNote[i])) == 0:
        #         return False
        #     else:
        #         d[ransomNote[i]] -= 1
        
        # return True