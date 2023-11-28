p1_count = 0
p2_count = 0

with open("input_4.txt") as f:
    for line in f.readlines():
        line = line.strip()
        [x, y] = line.split(",")

        [x_min, x_max] = x.split("-")
        [y_min, y_max] = y.split("-")

        x_min = int(x_min)
        x_max = int(x_max)
        y_min = int(y_min)
        y_max = int(y_max)

        print(f"{x_min}-{x_max}, {y_min}-{y_max}")

        if (x_min <= y_min and x_max >= y_max) or (y_min <= x_min and y_max >= x_max):
            print("It contains!!")
            p1_count += 1
        else:
            print("Not contained")
            print(x_min <= y_min and x_max >= y_max)
            print(y_min <= x_min and y_max >= x_max)

        if (x_min <= y_max and x_min >= y_min) or (y_min <= x_max and y_min >= x_min):
            p2_count += 1

print(f"P1: {p1_count}")
print(f"P2: {p2_count}")
