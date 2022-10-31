class Solution:
    def twoSum(self, nums, target):
        nums = list(zip(nums, range(len(nums))))

        nums.sort(key=lambda tup: tup[0]) 
        
        start, end = 0, len(nums)-1
        while start < end:
            sv = nums[start]
            ev= nums[end]
            current_sum = sv[0] + ev[0]
            if current_sum == target:
                return [sv[1], ev[1]]
            elif current_sum > target:
                end -= 1
            else:
                start += 1

if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([3,2,4], 6))
        
# Complexity
# python built-in sort: O(nlogn)
# while loop: O(n)
# Final complexity: O(nlogn)