def numIdenticalPairs(nums: list[int]) -> int:
    r: int = 0
    for i in range(len(nums)):
        if nums[i] in nums[i+1:]:
            r += nums[i+1:].count(nums[i])
    print(r)


numIdenticalPairs([1, 2, 3, 1, 1, 3])
