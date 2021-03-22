def binary_array_to_number(arr):
    result = 0
    a = 0
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == 1:
            result += 2**a
        a += 1
    return result


print(binary_array_to_number([0, 0, 0, 1]))
print(binary_array_to_number([0, 0, 1, 0]))
print(binary_array_to_number([1, 1, 1, 1]))
print(binary_array_to_number([0, 1, 1, 0]))
