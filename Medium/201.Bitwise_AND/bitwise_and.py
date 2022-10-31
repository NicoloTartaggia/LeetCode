class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i = 0 # count the number of different bits in the same position
        
        # >>= 1 shift bits to the right putting zero until 1 is reached
        while left != right:
            # 5 = 101 >>= 1 ==> 2 = 010 >>= 1 ==> 001 = 1 ==> STOP
            left >>= 1 
            # 7 = 111 >>= 1 ==> 3 = 011 >>= 1 ==> 001 = 1 ==> STOP
            right >>= 1
            i += 1
        # Two iterations for left = 5, right = 7 case. So i = 2.
        # n = 1 << 2 means move to the left putting one 0: 2 = 10 ==> 100 = 4
        return right << i