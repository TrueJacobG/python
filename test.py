def shuffle(nums, n):

    c = n - 1
    for i in range(n*2):
        if i % 2 != 0:
            nums.insert(i, nums[i+c])
            del nums[i+c+1]
            c -= 1

    return nums


print(shuffle([2, 5, 1, 3, 4, 7], 3))
