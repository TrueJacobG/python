def valid_parentheses(string):
    if string == "":
        return True
    brackets = []
    for element in string:
        if element == "(":
            brackets.append("(")
        if element == ")":
            try:
                brackets.pop()
            except:
                return False

    if len(brackets) == 0:
        return True
    else:
        return False


print(valid_parentheses("  ("))
print(valid_parentheses(")test"))
print(valid_parentheses(""))
print(valid_parentheses("hi())("))  # False
print(valid_parentheses("hi(hi)()"))
