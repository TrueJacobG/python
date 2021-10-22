def get_raw_filename(name):
    for i in range(len(name)-1, -1, -1):
        if name[i] == "/":
            return name[i+1:], name[:i]
    return name, "./"


def to_type(arg, t):
    error_message = "\033[93m" + \
        f"TYPE ERROR! YOU PUT WRONG INPUT in .py.test file!" + "\033[0m"
    if t == "int":
        try:
            return int(arg)
        except ValueError:
            print(error_message)
            exit()
    if t == "str":
        try:
            return str(arg)
        except ValueError:
            print(error_message)
            exit()
    if t == "float":
        try:
            return float(arg)
        except ValueError:
            print(error_message)
            exit()
    if t == "bool":
        try:
            return bool(arg)
        except ValueError:
            print(error_message)
            exit()
