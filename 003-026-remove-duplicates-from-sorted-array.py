nums = [1,1,2]

k = 0
new_array = []
for num in nums:
    if new_array == []:
        new_array.append(num)
    else:
        if num not in new_array:
            new_array.append(num)
        else:
            new_array.append("_")
print("rob", len(new_array), new_array)
nums = new_array
k = len(new_array)
print(k)