# 26.03.2021

def find_right_intervals(intervals):
    intervals.sort()
    result = []
    start_main, end_main = intervals[0][0], intervals[0][1]

    for count, interval in enumerate(intervals[1:]):
        start, end = interval[0], interval[1]
        if start > end_main:
            result.append([start_main, end_main])
            start_main, end_main = start, end
        else:
            end_main = max(end_main, end)

    result.append([start_main, end_main])
    return result


def sum_of_intervals(intervals):
    right_intervals = find_right_intervals(intervals)
    result = 0
    for start, end in right_intervals:
        result += end - start

    return result


print(sum_of_intervals([(1, 5)]))  # 4
print(sum_of_intervals([(1, 5), (6, 10)]))  # 8
print(sum_of_intervals([(1, 5), (1, 5)]))  # 4
print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))  # 7
