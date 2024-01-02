# https://leetcode.com/problems/sort-an-array/ 
# https://youtu.be/1dnNBcdNxYo
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                print(nums)
        return nums
    
nums = [4, 2, 7, 1, 5]
solution = Solution()
sorted_nums = solution.sortArray(nums)
print(sorted_nums)