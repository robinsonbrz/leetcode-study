# https://leetcode.com/problems/two-sum/

target = 10
nums = [1,6,38,94,5,6,7,8,9]

prev_map = {}

# for i, n in enumerate(nums):
#     diff = target - n
#     print(f"Diff {diff} n {n}")
#     if diff in prev_map:
#         print(f"{diff}", [prev_map[diff], i], f"{nums[diff]}{nums[i]}")
#     print(prev_map)
#     print()
#     prev_map[n] = i

n = len(nums)
for i in range(n):
    diff = target - nums[i]
    print(diff)
    if diff in prev_map:
        print(prev_map[diff], i)
        print(prev_map)
    prev_map[nums[i]] = i
