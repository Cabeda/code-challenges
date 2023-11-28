from enum import Enum


class Commands(Enum):
    CD = "$ cd"
    ls = "$ ls"


current_command: Commands
processing_output = True
dir_paths = {}
current_path = []

# Get string from path
def get_path(path: list[str]) -> str:
    if len(path) == 1:
        return "/"
    else:
        return f"/{'/'.join(path[1:])}"


with open("input_7.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        print(line)

        # 1. Understand if a new command is starting
        if line.startswith(str(Commands.CD.value)):
            current_command = Commands.CD
            processing_output = False

            # 2. Split is special as we get can extract the dir from the command
            [_, cd, dir] = line.split(" ")

            if dir == "..":
                current_path.pop()
            else:
                current_path.append(dir)

                path_name = get_path(current_path)
                # "Create a new path on the dictionary"
                if path_name not in dir_paths:
                    path_str = get_path(current_path)
                    dir_paths[path_str] = []

            path_name = get_path(current_path)
            print(path_name)

        elif line.startswith(str(Commands.ls.value)):
            current_command = Commands.ls
            processing_output = False
        else:
            processing_output = True

        if processing_output:
            match current_command:
                case Commands.ls:
                    if not line.startswith("dir"):
                        [size, _] = line.split(" ")
                        path_name = get_path(current_path)
                        dir_paths[path_name].append(int(size))


def solution_1(dir_paths):

    sums = 0

    for key in dir_paths:

        pathList = list(filter(lambda x: x.startswith(key), dir_paths))
        total = sum([sum(dir_paths[path]) for path in pathList])

        if total <= 100000:
            sums += total

    print(f"The final sum is {sums}")


def solution_2(dir_paths):

    total_space = 70000000
    unused_space = 30000000

    totals = []
    # Totals that by removing get us enough space
    totals_removable = []

    for key in dir_paths:

        pathList = list(filter(lambda x: x.startswith(key), dir_paths))
        total = sum([sum(dir_paths[path]) for path in pathList])
        print(f"{key} has {total}")
        totals.append(total)

    print(f"Max size is {max(totals)}")
    print(f"Free space of {total_space - max(totals)}")

    for total in totals:
        if total_space - max(totals) + total > unused_space:
            totals_removable.append(total)

    print(f"The minimum dir to remove is {min(totals_removable)}")


solution_2(dir_paths)
