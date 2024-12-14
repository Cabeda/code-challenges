with open("input.txt") as f:
    lines = f.readlines()
    reports = [x.split() for x in lines]

safes = 0
for report in reports:
    dampened = False
    trend = None
    i = 0
    while i < len(report) - 1:
        curr = int(report[i])
        nex = int(report[i + 1])
        diff = nex - curr

        if abs(diff) > 3 or diff == 0:
            if not dampened:
                dampened = True
                i += 1
                continue
            else:
                print(f"Report {report} is not safe.")
                break

        if trend is None:
            trend = 'increasing' if diff > 0 else 'decreasing'
        else:
            if (trend == 'increasing' and diff < 0) or (trend == 'decreasing' and diff > 0):
                if not dampened:
                    dampened = True
                    i += 1
                    continue
                else:
                    print(f"Report {report} is not safe.")
                    break

        i += 1
    else:
        safes += 1
        if dampened:
            print(f"Report {report} is safe but was dampened")
        else:
            print(f"Report {report} is safe")

print(safes)
