def convertToPriority(char: str) -> int:
    if char.islower():
        return ord(char) - ord("a") + 1
    else:
        return ord(char) - ord("A") + 27


chars = []
priorities = []

with open("input_3.txt", "r") as f:
    for line in f.readlines():
        line_clean = line.strip()
        line_length = len(line_clean)
        line_cut = int(line_length / 2)
        first_compartment = line_clean[:line_cut]
        second_compartment = line_clean[line_cut:]

        for char in first_compartment:
            exists = second_compartment.find(char)
            if exists != -1:
                num_occurrences = line_clean.count(char)
                priority = convertToPriority(char)
                print(f"{first_compartment} {second_compartment}")
                print(
                    f"Common item is {char}, occured {num_occurrences} times -> {priority}\n"
                )
                chars.append(char)
                priorities.append(priority)
                break


total = sum(priorities)

print(f"The total is {total}")


chars_groups = []
chars_group = []
sum_p2 = 0

with open("input_3.txt", "r") as f:

    for line in f.readlines():
        line_clean = line.strip()

        chars_group.append(line_clean)

        # Only do the computation when we have 3 ruddersacks
        if len(chars_group) == 3:

            (x,) = set(chars_group[0]) & set(chars_group[1]) & set(chars_group[2])

            print(f"Common in the three is {x}")

            sum_p2 += convertToPriority(x)
            # Empty chas_group at the end
            chars_group = []

print(f"Total of p2 is {sum_p2}")
