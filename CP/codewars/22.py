def solution(string, markers):
    lines = string.split("\n")
    for number, line in enumerate(lines):
        for m in markers:
            i = line.find(m)
            if i != -1:
                line = line[:i]
        lines[number] = line.rstrip(" ")
    return "\n".join(lines)


print(solution("apples, pears # and bananas\ngrapes\nbananas !apples",
               ["#", "!"]))  # "apples, pears\ngrapes\nbananas"

print("##################")
print(solution("a #b\nc\nd $e f g", ["#", "$"]))  # "a\nc\nd"
