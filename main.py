##x1mv\\2022\\projectname;FUNCTEST;version:1.0\

import os

f = open("functionoutput.txt", "w")
file_exists = os.path.exists("functionoutput.txt")

print("- CHINESE GOVERNMENT -")
asd = input("type some random shit dawg: ")

def testing():
    f.write(asd)
    f.close()

testing()

x = input("enter to exit")
