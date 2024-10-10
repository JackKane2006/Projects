def twoSum(nums, target):
    dict = {}
    for index, val in enumerate(nums):
        if val in dict.values():
            return [list(dict.values()).index(val), index]
        dict[index] = target - val
    return []

array = [2, 7, 8, 9]
target = 17
print(twoSum(array, target))
