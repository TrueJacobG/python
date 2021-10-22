import argparse
import sys
import subprocess
from lib import get_raw_filename, to_type


def get_functions_in_py(file_txt):
    functions_in_py = []
    funcs_count = file_txt.count("def")

    i = 0
    while funcs_count != 0:
        func = []
        df = file_txt.index("def", i)
        bracket_open = file_txt.index("(", i)
        bracket_close = file_txt.index(")", i)
        arrow = file_txt.index(">", i)
        colon = file_txt.index(":", arrow)

        func.append(file_txt[df+4:bracket_open])

        args_types = ""
        args = file_txt[bracket_open+1:bracket_close]
        args_colons = args.count(":")
        i = 0
        last_comma_i = -2
        comma_i = -1
        while args_colons != 0:
            args_colon_i = args.index(":", i)
            if last_comma_i != comma_i:
                comma_i = args.index(",", i)
                last_comma_i = comma_i
            else:
                comma_i = len(args)

            args_types += args[args_colon_i+2:comma_i] + ";"

            i = comma_i
            args_colons -= 1

        func.append(args_types + file_txt[arrow+2:colon])
        functions_in_py.append(func)

        i = colon
        funcs_count -= 1

    return functions_in_py


def import_python_file():
    # Parse file
    parser = argparse.ArgumentParser("-h")
    parser.add_argument("file", metavar="FILE", type=str,
                        help="file to test should look like fortest.py")
    parser.add_argument("-live", action="store_true",
                        help="if you want to see passing tests give the flag")
    parser.add_argument("-types", action="store_true",
                        help="if you want to see if types are correct give the flag")
    args = parser.parse_args()

    info = {"filename": args.file, "live": args.live, "types": args.types}

    # now file is imported :D
    # exec(open(args.file).read())

    with open(info["filename"], 'r') as f:
        file_txt = f.read()

    # get functions from file.py
    functions_in_py = get_functions_in_py(file_txt)

    return info, functions_in_py


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


def import_test_file(name):
    with open(name+".test", 'r') as f:
        file_txt = f.readlines()

    types_lst = []

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
            types_lst.append([func, types])
            need_name = False
            continue

        if line.strip() == "":
            need_name = True
            continue

        args, res = get_args_results(line.strip(), types)

        expectations.append([func, args, res])

    return expectations, types_lst


def testing_with_mypy(filename):
    try:
        x = subprocess.run(["mypy", filename])
    except:
        print("\033[91m" +
              f"YOU HAVE TO INSTALL MYPY" + "\033[0m")
        exit()

    if x.returncode != 0:
        print("\033[91m" +
              f"MYPY DETECTED TYPE ERROR IN {filename}" + "\033[0m")
        exit()


def vis_type_inputs(expects):
    for i in range(len(expects)):
        func = expects[i][0]
        line = []
        for arg in expects[i][1]:
            line.append(str(type(arg)).replace(
                "<class '", "").replace("'>", ""))
        for res in expects[i][2]:
            line.append(str(type(res)).replace(
                "<class '", "").replace("'>", ""))

        args = expects[i][1] + expects[i][2]

        print(
            "\033[94m" + f"{args} are {line}" + "\033[0m")


def testing_test_file(in_py, in_test, expects, flag):
    if in_py != in_test:
        for i in range(0, len(in_test)):
            if in_py[i][1] != in_test[i][1]:
                print(
                    "\033[91m" + f"TYPE ERROR! {in_test[i][0]} -> {in_test[i][1]} SHOULD BE EQUAL TO {in_py[i][1]}" + "\033[0m")
                exit()
    if flag:
        vis_type_inputs(expects)
        print("\033[94mTYPES and FUNCS IN .py AND .py.test ARE EQUAL\033[0m")


def test_function(info, expectations):
    rawname, path = get_raw_filename(info["filename"])

    sys.path.insert(1, path)

    module = __import__(rawname[:-3])
    ok = True
    for x in expectations:
        try:
            result = getattr(module, x[0])(*x[1])
        except AttributeError:
            print(
                "\033[93m" + f"You put wrong function in {info['filename']}.test" + "\033[0m")
            exit()

        if [result] != x[2]:
            ok = False
            print(
                f"\033[91mWARNING! {x[0]} -> {x[1]} should give {x[2]}, but instead gave {[result]}\033[0m")
            if info["live"]:
                break

        if info["live"]:
            print(f"\033[92m{x[0]} args->{x[1]} res->{x[2]}\033[0m")

    if ok:
        print("\033[92mEVERYTHING OK!\033[0m")


def main():
    info, functions_in_py = import_python_file()
    expects, functions_in_test = import_test_file(info["filename"])

    testing_with_mypy(info["filename"])

    testing_test_file(functions_in_py, functions_in_test, expects,
                      info["types"])

    test_function(info, expects)


if __name__ == '__main__':
    main()
