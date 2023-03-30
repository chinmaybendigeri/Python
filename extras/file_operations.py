import os
import shutil


print(os.getcwd()) # to get the current working dir for python
print(os.listdir())  # to list all the files and folders in the current working dir

for folder, subfolders, files in os.walk('/oops'):

    print(f"I am currently at {folder}")

    print(f"There are following files in it: ")
    for pos, file in enumerate(files):
        print(f"File {pos} is {file}")

    print(f"There are following sub directories in it: ")
    for pos, sub_fold in enumerate(subfolders):
        print(f"File {pos} is {sub_fold}")

shutil.move(os.getcwd(), '/resources')  # shutil command helps to move files from one dir to another dir and also
# perform few other complex operations

