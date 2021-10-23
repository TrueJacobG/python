import argparse
import sys
import subprocess
from lib import get_raw_filename, to_type, say, get_args_and_results, py_file_scraping


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
    functions_in_py = py_file_scraping(file_txt)

    return info, functions_in_py


def import_test_file(name):
    try:
        with open(name+".test", 'r') as f:
            file_txt = f.readlines()
    except:
        say(f"ERROR! NO .py.test FILE IN DIRECTORY!", "y")
        exit()

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

        args, res = get_args_and_results(line.strip(), types)

        expectations.append([func, args, res])

    return expectations, types_lst


def testing_with_mypy(filename):
    try:
        x = subprocess.run(["mypy", filename])
    except:
        say(f"YOU HAVE TO INSTALL MYPY", "r")
        exit()

    if x.returncode != 0:
        say(f"MYPY DETECTED TYPE ERROR IN {filename}", "g")
        exit()


def visualize_input_types(expects):
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

        say(f"{args} are {line}", "b")


def testing_test_file(in_py, in_test, expects, flag):
    if in_py != in_test:
        for i in range(0, len(in_test)):
            if in_py[i][1] != in_test[i][1]:
                say(f"TYPE ERROR! {in_test[i][0]} -> {in_test[i][1]} SHOULD BE EQUAL TO {in_py[i][1]}", "r")
                exit()
    if flag:
        visualize_input_types(expects)
        say("TYPES and FUNCS IN .py AND .py.test ARE EQUAL", "b")


def test_function(info, expectations):
    rawname, path = get_raw_filename(info["filename"])

    sys.path.insert(1, path)

    module = __import__(rawname[:-3])
    ok = True
    for x in expectations:
        try:
            result = getattr(module, x[0])(*x[1])
        except AttributeError:
            say(f"You put wrong function in {info['filename']}.test", "y")
            exit()

        if [result] != x[2]:
            ok = False
            say(
                f"WARNING! {x[0]} -> {x[1]} should give {x[2]}, but instead gave {[result]}", "r")
            if info["live"]:
                break

        if info["live"]:
            say(f"{x[0]} args->{x[1]} res->{x[2]}", "g")

    if ok:
        say("EVERYTHING OK!", "g")


def main():
    info, functions_in_py = import_python_file()
    expects, functions_in_test = import_test_file(info["filename"])

    testing_with_mypy(info["filename"])

    testing_test_file(functions_in_py, functions_in_test, expects,
                      info["types"])

    test_function(info, expects)


if __name__ == '__main__':
    main()
