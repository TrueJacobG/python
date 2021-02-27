def solution(s):
    result = ""
    for i in s:
        if i.isupper():
            result += " "
            result += i
        else:
            result += i
    return result


print(solution("helloWorld"))
print(solution("camelCase"))
print(solution("breakCamelCase"))
