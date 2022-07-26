'''
Prints list of incompletely downloaded spaces after using confluence-dumper

Usage: python incomplete_spaces.py [-r]
Optional args:
[-r]    if flag set, will remove folders of incomplete spaces
'''
import os
import sys
import shutil

spaces_folder = "extra/" # folder where all spaces are saved
incomplete_spaces = [] # store list of incomplete spaces

# parse args from command line
if len(sys.argv) > 2:
    print("\nUsage: python incomplete_spaces.py [-r]\n")
    print("Optional args:\n[-r]\tif flag set, will remove folders of incomplete spaces\n")
    sys.exit(0)

remove = False
if len(sys.argv) == 2 and sys.argv[1] == "-r":
    remove = True

for folder in os.scandir(spaces_folder):
    path = folder.path
    attachments = path + "/attachments"

    if os.path.exists(attachments): # get space name if attachments folder still there
        f_name = os.path.basename(path)
        space = os.path.splitext(f_name)[0]
        incomplete_spaces.append(space)

print("There are {} incomplete spaces:".format(len(incomplete_spaces)))
print(incomplete_spaces)

# remove folder if -r flag set
if remove:
    print("\nRemoving incomplete space folders...")
    for space in incomplete_spaces:
        space_path = spaces_folder + space
        try:
            shutil.rmtree(space_path)
        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))

    print("Done!")