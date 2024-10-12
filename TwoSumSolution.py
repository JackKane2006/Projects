#leetcode easy difficulty problem, https://leetcode.com/problems/two-sum/description/
#given a list of numbers and a target number, find the two numbers in the list that add up to the target
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
