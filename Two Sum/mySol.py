def twoSum(nums, target):
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums):
            if i != j:
                if num1 + num2 == target:
                    return [i, j]