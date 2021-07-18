import os
import shutil

for x in os.walk("copyyy"):
    if "venv" in x[1]:
        path = x[0]+"\\venv"
        shutil.rmtree(path)
        print("DONE v")
    if ".idea" in x[1]:
        path = x[0]+"\\.idea"
        shutil.rmtree(path)
        print("DONE i")
