import argparse
import sys
import subprocess
from lib import get_raw_filename, say, get_args_and_results, py_file_scraping, visualize_input_types
from inspect import currentframe, getframeinfo


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
            cl = getframeinfo(currentframe())
            say(f"ERROR! NO .py.test FILE IN DIRECTORY!", "y", cl.lineno)
            exit()

        functions_in_test = {}

        expects = []
        need_name = True
        for line in file_txt:
            if need_name:
                try:
                    t = line.index(";")
                except ValueError:
                    cl = getframeinfo(currentframe())
                    say(
                        f"You have to put TYPES in {self.flags['filename']}.test", "y", cl.lineno)
                    exit()
                func = line.strip()[:t]
                types = line.strip()[t+1:]
                functions_in_test[func] = types
                need_name = False
                continue

            if line.strip() == "":
                need_name = True
                continue

            if func not in self.functions_in_py.keys():
                continue

            args, res = get_args_and_results(line.strip(), types)

            expects.append([func, args, res])

        return expects, functions_in_test

    def testing_with_mypy(self):
        try:
            x = subprocess.run(["mypy", self.flags["filename"]])
        except:
            cl = getframeinfo(currentframe())
            say(f"YOU HAVE TO INSTALL MYPY", "r", cl.lineno)
            exit()

        if x.returncode != 0:
            cl = getframeinfo(currentframe())
            say(
                f"MYPY DETECTED TYPE ERROR IN {self.flags['filename']}", "r", cl.lineno)
            exit()

    def testing_test_file(self):
        in_py = self.functions_in_py
        in_test = self.functions_in_test

        if in_py != in_test:
            for key in in_test.keys():
                if key not in in_py.keys():
                    cl = getframeinfo(currentframe())
                    say(
                        f"ERROR! THERE IS NO {key} FUNC IN {self.flags['filename']}", "r", cl.lineno)
                    exit()

                if in_py[key] != in_test[key]:
                    cl = getframeinfo(currentframe())
                    say(
                        f"TYPE ERROR! {key} -> {in_test[key]} SHOULD BE EQUAL TO {in_py[key]}", "r", cl.lineno)
                    exit()
        if self.flags["types"]:
            visualize_input_types(self.expects)
            cl = getframeinfo(currentframe())
            say("TYPES and FUNCS IN .py AND .py.test ARE EQUAL", "b", cl.lineno)

    def test_function(self):
        rawname, path = get_raw_filename(self.flags["filename"])

        sys.path.insert(1, path)

        module = __import__(rawname[:-3])
        ok = True
        for x in self.expects:
            out = getattr(module, x[0])(*x[1])

            args = " ".join([str(arg) for arg in x[1]])
            results = " ".join([str(res) for res in x[2]])
            if [out] != x[2]:
                ok = False
                cl = getframeinfo(currentframe())
                say(
                    f"WARNING! {x[0]} -> {args} should give {results}, but instead gave {out}", "r", cl.lineno)
                if self.flags["live"]:
                    break

            if self.flags["live"]:
                cl = getframeinfo(currentframe())
                say(f"{x[0]} args-> {args} res-> {results}", "g", cl.lineno)

        if ok:
            cl = getframeinfo(currentframe())
            say("EVERYTHING OK!", "g", cl.lineno)


def main():
    test = TestingTool()


if __name__ == '__main__':
    main()
