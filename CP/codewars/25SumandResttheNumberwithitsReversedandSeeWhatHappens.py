
def sum_dif_rev(num):
    count = 36
    while num:
        count += 9
        if count % 10 == 0:
            continue
        reverseN = int(str(count)[::-1])
        if count != reverseN and (count + reverseN) % abs(count - reverseN) == 0:
            num -= 1
    return count


print(sum_dif_rev(17))  # 45
print(sum_dif_rev(3))  # 495
print(sum_dif_rev(4))  # 594
