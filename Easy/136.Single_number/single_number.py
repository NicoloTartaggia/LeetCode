class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #Time complexity = O(n) -> OK
        #Space complexity = O(n) -> NOT OK. In case of [1,2,3,4,1,2,3,4] our dict will contain the
        #1,2,3,4 before starting to remove elements, which leads to O(n)
        #m = {}
        #for n in nums:
        #    if m.get(n, None) == None:
        #        m[n] = 1
        #    else:
        #        m.pop(n)
        #return list(m)[0]
        
        #Solution respecting the costraints
        #xor is commtative and associative:
        # 1 xor 2 xor 3 xor 1 xor 2 xor 3 xor 4 = (1 xor 1) xor (2 xor 2) xor (3 xor 3) xor 4 
        # = 0 xor 0 xor 0 xor 4 = 4
        xor = 0
        for n in nums:
            xor = xor ^ n
        return xor