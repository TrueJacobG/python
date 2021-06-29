def minOperations(nums):
    if len(nums) == 1:
        return 0
    result = 0
    for i in range(1, len(nums)):
        if nums[i-1] >= nums[i]:
            x = nums[i-1] - nums[i] + 1
            nums[i] += x
            result += x

    return result


print(minOperations([1, 5, 2, 4, 1]))
