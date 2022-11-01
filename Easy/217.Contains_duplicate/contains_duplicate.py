class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        found = {}
        for n in nums:
            if n in found:
                return True
            else:
                found[n] = True
        return False