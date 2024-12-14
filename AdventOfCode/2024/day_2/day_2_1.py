with open('input.txt') as f:
    lines = f.readlines()
    reports = [x.split() for x in lines]


safes = 0
for report in reports:
    typeDiff = int(report[0]) - int(report[1]) 
    print("typeDiff: ", typeDiff)
    print("report: ", report)
    for i in range(len(report)-1):
        diff = int(report[i]) - int(report[i+1]) 

        if abs(diff) > 3 or diff == 0:
            print(f"Report {report} is not safe")
            break

        if typeDiff > 0 and diff < 0:
            print(f"Report {report} is not safe")
            break

        if typeDiff < 0 and diff > 0:
            print(f"Report {report} is not safe")
            break
    
        if i == len(report) - 2:
            print(f"Report {report} is safe")
            safes += 1

print(safes)