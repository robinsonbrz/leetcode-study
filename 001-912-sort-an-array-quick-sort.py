# https://leetcode.com/problems/sort-an-array/ 

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def quick_sort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            print("Pivot", pivot)
            left = [x for x in arr if x < pivot]
            print("Left", left)
            middle = [x for x in arr if x == pivot]
            print("Middle", middle)
            right = [x for x in arr if x > pivot]
            print("Right", right)
            return quick_sort(left) + middle + quick_sort(right)

        return quick_sort(nums)

nums = [4, 2, 7, 1, 5]
solution = Solution()
sorted_nums = solution.sortArray(nums)
print(sorted_nums)