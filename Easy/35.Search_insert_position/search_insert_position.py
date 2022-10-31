class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, n in enumerate(nums):
            if nums[i] >= target:
                return i
        return len(nums)