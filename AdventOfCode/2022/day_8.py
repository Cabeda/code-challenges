def get_distance(row: list[int], tree_value: int) -> int:
    distance = 0
    for item in row:
        distance += 1
        if item >= tree_value:
            break

    return distance


with open("input_8.txt", "r") as f:
    lines = [list(line.strip()) for line in f.readlines()]

    total_hidden = 0
    total_seens = 0
    max_distance = 0

    for i in range(1, len(lines) - 1):
        for j in range(1, len(lines[i]) - 1):
            tree_spot = int(lines[i][j])
            col = [line[j] for line in lines]
            row = list(lines[i])
            row_before = list(map(int, row[:j]))
            row_after = list(map(int, row[j + 1 :]))
            col_before = list(map(int, col[:i]))
            col_after = list(map(int, col[i + 1 :]))

            adjacents = [
                max(row_before),
                max(row_after),
                max(col_before),
                max(col_after),
            ]

            distance = (
                get_distance(row_before[::-1], tree_spot)
                * get_distance(row_after, tree_spot)
                * get_distance(col_before[::-1], tree_spot)
                * get_distance(col_after, tree_spot)
            )

            if distance > max_distance:
                max_distance = distance

            if tree_spot <= min(adjacents):
                print(f"[{i+1},{j+1}] is hidden. {adjacents}")
                total_hidden += 1
            else:
                print(f"[{i+1},{j+1}] is visible. {adjacents}")
                total_seens += 1

print(f"Total hidden spots: {total_hidden}")
print(f"Total seen from outside spots: {len(lines) * len(lines) - total_hidden }")
print(f"Max distance is of: {max_distance}")
