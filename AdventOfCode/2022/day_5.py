def stacker_9000(stacks, moves):
    print("Starting moves with stacker_90010")
    print(moves)
    print(stacks)
    for move in moves:
        for _ in range(0, int(move[1])):
            print(f"Moving from {move[3]} to {move[5]}")
            el = stacks[int(move[3]) - 1].pop(0)
            stacks[int(move[5]) - 1].insert(0, el)

    print(stacks)

    result = ""
    for col in stacks:
        result += col[0]

    print(f"The final result at the top of the stacks with model 9000: {result}")


# Stacker can move multiples crates in a col at the same time
def stacker_9001(stacks, moves):
    print("Starting moves with stacker_9001")
    print(moves)
    print(stacks)
    for move in moves:
        print(f"Moving {int(move[1])} crates from {move[3]} to {move[5]}")
        els = stacks[int(move[3]) - 1][:int(move[1])]
        stacks[int(move[5]) - 1] = els + stacks[int(move[5]) - 1]
        del stacks[int(move[3]) - 1][:int(move[1])]

    print(stacks)

    result = ""
    for col in stacks:
        result += col[0]

    print(f"The final result at the top of the stacks with model 9000: {result}")


moves = []
# A grid where we represent for each cell a crate.
# The row is the crate level and the column the stack
stacks = []
ended_stack = False
with open("input_5.txt", "r") as f:
    for line in f.readlines():
        line = line.replace("\n", "")
        if ended_stack is False:
            if len(line) > 1:
                n = 4
                cols = [
                    line[i : i + n].strip().replace("[", "").replace("]", "")
                    for i in range(0, len(line), n)
                ]

                # Initialize the stack cols
                if len(stacks) == 0:
                    stacks = [[] for col in cols]

                for index_col in range(0, len(cols)):
                    if cols[index_col] != "":
                        stacks[index_col].append(cols[index_col])

            else:
                # Start to store moves instead of stacks
                ended_stack = True
        else:
            move = line.split(" ")
            moves.append(move)


# stacker_9000(stacks, moves)
stacker_9001(stacks, moves)
