class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Two-pointers technique
        slow = 0 # index of the left-most zero
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            if nums[slow] != 0:
                slow += 1
        
        # Example
        # nums = [0,1,0,3,12]
        # 
        # Iteration 0
        # slow = fast = 0
        # nums[slow] = nums[fast] = 0
        # No swap. No slow increase. Nums unchanged.
        
        # Iteration 1
        # slow = 0, fast = 1
        # nums[slow] = 0, nums[fast] = 1
        # Swap. Slow increases. Nums = [1,0,0,3,12].
        
        # Iteration 2
        # slow = 1, fast = 2
        # nums[slow] = nums[fast] = 0
        # No swap. No slow increase. Nums unchanged.
        
        # Iteration 3
        # slow = 1, fast = 3
        # nums[slow] = 0, nums[fast] = 3
        # Swap. Slow increases. Nums = [1,3,0,0,12].
        
        # Iteration 4
        # slow = 2, fast = 4
        # nums[slow] = 0, nums[fast] = 12
        # Swap. Slow increases. Nums = [1,3,12,0,0].