'''
Checks for duplicate space folders after using confluence dumper

Usage: python check_duplicates.py
'''
import os

# the two folders you want to check
folder1 = "export/export_all2/"
folder2 = "export/export_all4/"

spaces1 = os.listdir(folder1)
spaces2 = os.listdir(folder2)

duplicates = [] # keep track of duplicates
for space in spaces2:
    if space in spaces1:
        duplicates.append(space)

print("There are {} duplicate spaces in folders: {} & {}".format(
    len(duplicates), folder1, folder2))
print(duplicates)