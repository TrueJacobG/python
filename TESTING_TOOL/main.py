import argparse
import sys
import subprocess
from lib import get_raw_filename, say, get_args_and_results, py_file_scraping, visualize_input_types


class TestingTool:
    def __init__(self):
        self.flags, self.functions_in_py = self.import_python_file()
        self.expects, self.functions_in_test = self.import_test_file()

        self.testing_with_mypy()

        self.testing_test_file()

        self.test_function()

    def import_python_file(self):
        # Parse file
        parser = argparse.ArgumentParser("-h")
        parser.add_argument("file", metavar="FILE", type=str,
                            help="file to test should look like fortest.py")
        parser.add_argument("-live", action="store_true",
                            help="if you want to see passing tests give the flag")
        parser.add_argument("-types", action="store_true",
                            help="if you want to see if types are correct give the flag")
        args = parser.parse_args()

        flags = {"filename": args.file, "live": args.live, "types": args.types}

        # now file is imported :D
        # exec(open(args.file).read())

        with open(flags["filename"], 'r') as f:
            file_txt = f.read()

        # get functions from file.py
        functions_in_py = py_file_scraping(file_txt)

        return flags, functions_in_py

    def import_test_file(self):
        try:
            with open(self.flags["filename"]+".test", 'r') as f:
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
                        "\033[93m" + f"You have to put TYPES in {self.flags['filename']}.test" + "\033[0m")
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

    def testing_with_mypy(self):
        try:
            x = subprocess.run(["mypy", self.flags["filename"]])
        except:
            say(f"YOU HAVE TO INSTALL MYPY", "r")
            exit()

        if x.returncode != 0:
            say(f"MYPY DETECTED TYPE ERROR IN {self.flags['filename']}", "g")
            exit()

    def testing_test_file(self):
        in_py = self.functions_in_py
        in_test = self.functions_in_test
        if in_py != in_test:
            for i in range(0, len(in_test)):
                if in_py[i][1] != in_test[i][1]:
                    say(
                        f"TYPE ERROR! {in_test[i][0]} -> {in_test[i][1]} SHOULD BE EQUAL TO {in_py[i][1]}", "r")
                    exit()
        if self.flags["types"]:
            visualize_input_types(self.expects)
            say("TYPES and FUNCS IN .py AND .py.test ARE EQUAL", "b")

    def test_function(self):
        rawname, path = get_raw_filename(self.flags["filename"])

        sys.path.insert(1, path)

        module = __import__(rawname[:-3])
        ok = True
        for x in self.expects:
            try:
                result = getattr(module, x[0])(*x[1])
            except AttributeError:
                say(
                    f"You put wrong function in {self.flags['filename']}.test", "y")
                exit()

            if [result] != x[2]:
                ok = False
                say(
                    f"WARNING! {x[0]} -> {x[1]} should give {x[2]}, but instead gave {[result]}", "r")
                if self.flags["live"]:
                    break

            if self.flags["live"]:
                say(f"{x[0]} args->{x[1]} res->{x[2]}", "g")

        if ok:
            say("EVERYTHING OK!", "g")


def main():
    test = TestingTool()


if __name__ == '__main__':
    main()
