'''
Counts and lists all spaces which have been exported
Also checks to see if any spaces have been missed from a list

Usage: python count_spaces.py
'''
import os 

export_folder = "export/" # folder containing all exported spaces
spaces_list = "export/all_spaces.txt" # file containing list of expected spaces

# generate list of exported spaces
def list_exported():
    exported_spaces = []
    for item in os.listdir(export_folder):
        path = export_folder + item

        if os.path.isdir(path):
            # count & list spaces for each subfolder
            sub_folder = os.listdir(path)
            for space in sub_folder:
                exported_spaces.append(space)
    return exported_spaces

# generate list of expected spaces
def list_expected():
    expected_spaces = []
    with open(spaces_list, "r") as f:
        text = f.read()
        start_ind = text.index("space(s)") + 11
        text = text[start_ind:] # jump to start of list

        expected_spaces = text.split(", ")
        return expected_spaces

# generate list of missing spaces
def list_missing(expected, exported):
    missing_spaces = []
    for space in expected:
        space = space.replace("\n", "") # check for new line characters
        if space not in exported:
            missing_spaces.append(space)

    return missing_spaces

# main method
if __name__ == "__main__":
    expected_spaces = list_expected()
    print("{} spaces are expected in this wiki".format(len(expected_spaces)))

    exported_spaces = list_exported()
    print("{} spaces have been exported".format(len(exported_spaces)))

    missing_spaces = list_missing(expected_spaces, exported_spaces)
    print("{} spaces are missing".format(len(missing_spaces)))
    print(missing_spaces)