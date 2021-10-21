import argparse
import sys


def get_functions(file):
    functions = []
    funcs_count = file.count("def")

    i = 0
    while funcs_count != 0:
        func = []
        df = file.index("def", i)
        bracket_open = file.index("(", i)
        bracket_close = file.index(")", i)

        func.append(file[df+4:bracket_open])
        func.append(file[bracket_open+1:bracket_close])
        functions.append(func)

        i = bracket_close
        funcs_count -= 1

    return functions


def import_python_file():
    # Parse file
    parser = argparse.ArgumentParser("-h")
    parser.add_argument("file", metavar="FILE", type=str,
                        help="file to test should look like fortest.py")
    parser.add_argument("-live", action="store_true",
                        help="if you want to see passing tests give the flag")
    args = parser.parse_args()

    options = {"filename": args.file, "live": args.live}

    # now file is imported :D
    # exec(open(args.file).read())

    with open(options["filename"], 'r') as f:
        file_txt = f.read()

    # get functions from file
    functions = get_functions(file_txt)

    return options, functions


def to_type(arg, t):
    if t == "int":
        return int(arg)
    if t == "str":
        return str(arg)
    if t == "float":
        return float(arg)
    if t == "bool":
        return bool(arg)


def get_args_results(line, types):
    line = line.split(";")
    types = types.split(";")

    args = []
    results = []
    i = 0

    for arg in line[0].split(","):
        args.append(to_type(arg, types[i]))
        i += 1

    for res in line[1].split(","):
        results.append(to_type(res, types[i]))
        i += 1

    return args, results


def get_expectations(name):
    with open(name+".test", 'r') as f:
        file_txt = f.readlines()

    expectations = []
    need_name = True
    for line in file_txt:
        if need_name:
            try:
                t = line.index(";")
            except ValueError:
                print(
                    "\033[93m" + f"You have to put TYPES in {name}.test" + "\033[0m")
                exit()
            func = line.strip()[:t]
            types = line.strip()[t+1:]
            need_name = False
            continue

        if line.strip() == "":
            need_name = True
            continue

        args, res = get_args_results(line.strip(), types)

        expectations.append([func, args, res])

    return expectations


def get_raw_filename(name):
    for i in range(len(name)-1, -1, -1):
        if name[i] == "/":
            return name[i+1:], name[:i]
    return name, "./"


def test_function(options, expectations):
    rawname, path = get_raw_filename(options["filename"])

    sys.path.insert(1, path)

    module = __import__(rawname[:-3])
    ok = True
    for x in expectations:
        try:
            result = getattr(module, x[0])(*x[1])
        except AttributeError:
            print(
                "\033[93m" + f"You put wrong function in {options['filename']}.test" + "\033[0m")
            exit()

        if [result] != x[2]:
            ok = False
            print(
                f"\033[91mWRONG! {x[0]} -> {x[1]} should give {x[2]}, but instead gave {[result]}\033[0m")
            if options["live"]:
                break

        if options["live"]:
            print(f"\033[92m{x[0]} args->{x[1]} res->{x[2]}\033[0m")

    if ok:
        print("\033[92mEVERYTHING OK!\033[0m")


def main():
    options, functions = import_python_file()
    expectations = get_expectations(options["filename"])

    test_function(options, expectations)


if __name__ == '__main__':
    main()
