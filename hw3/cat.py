import sys
from pathlib import Path
from colorama import Fore, init


def print_tree(path: Path , indent: int =1) -> None:

    """Printing the durectory structure in colors (if a directory located inside the current one) with spaces added to each subfolder and file"""

    path = Path(path)

    for item in path.iterdir():

        if item.is_dir(): #checking if a part of the path is a directory
            print("    " * indent + Fore.GREEN + item.name) #printing directory name in green
            print_tree(item, indent + 1) #recursion - performing the same process for the given directory, with adding spaces indentation

        else:
            print("    " * indent + Fore.RED + item.name) #if it´s a folder, printing in red with more spaces


if __name__ == "__main__": #testing the fuction
    if len(sys.argv) < 2:  # checks if directory name is added
        print("Use following command: python cat.py <directory>")
        sys.exit()

    init(autoreset=True)  # resettimg the colors to default after each print

    root = Path(sys.argv[1])

    print(Fore.BLUE + root.name)  # orinting the name of seletced directory before the rest of the structure is returned by the function

    print_tree(root)