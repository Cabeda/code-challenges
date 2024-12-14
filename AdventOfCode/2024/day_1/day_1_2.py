with open('input_1.txt') as f:
    lines = f.readlines()
    a = [x.split() for x in lines]

list1, list2 = list(zip(*a))

print(list1)
print(list2)
list1 = [int(x) for x in list1]
list2 = [int(x) for x in list2]

similarity = []
for num in list1:
    total = len([x for x in list2 if num == x])
    similarity.append( num *total)

sum(similarity)

