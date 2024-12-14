# import txt file



with open('input_1.txt') as f:
    lines = f.readlines()
    a = [x.split() for x in lines]

list1, list2 = list(zip(*a))

print(list1)
print(list2)
list1 = [int(x) for x in list1]
list2 = [int(x) for x in list2]

list1 = sorted(list1)
list2 = sorted(list2)

diffs = []
for i in range(len(list1)):
    diffs.append(abs(list2[i] - list1[i]))

sum(diffs)

