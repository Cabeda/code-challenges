elves_cals = []
max = 0

with open("day_1.txt", "r") as f:
    count = 0
    for line in f.readlines():
        if len(line) > 1:
            count = count + int(line)
        else:
            print(f"New elf! Previous one got {count}")
            elves_cals.append(count)
            count = 0

        if max < count:
            max = count
            print(f"New max is {max}")

print(f"The elf with max calories got {max}")


ranks = sorted(elves_cals, reverse=True)


total_top_3 = sum(ranks[0:3])

print(f"The total of the top 3 was {total_top_3}")
