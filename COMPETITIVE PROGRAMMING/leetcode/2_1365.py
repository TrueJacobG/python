def smallerNumbersThanCurrent(nums: list) -> list:
    result: list = []
    sor: list = sorted(nums)
    for i in range(len(nums)):
        c: int = sor.index(nums[i])
        result.append(c)
    return result


print(smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
