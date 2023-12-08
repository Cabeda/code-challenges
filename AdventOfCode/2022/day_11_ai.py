class Monkey:
    def __init__(self, items, operation, test, throw_to):
        self.items = items
        self.operation = operation
        self.test = test
        self.throw_to = throw_to
        self.count = 0

    def inspect(self):
        new_items = []
        for item in self.items:
            self.count += 1
            new_item = self.operation(item)
            new_item //= 3
            new_items.append((new_item, self.throw_to[new_item % self.test == 0]))
        self.items = []
        return new_items

monkeys = [
    Monkey([63, 57], lambda x: x * 11, 7, [6, 2]),
    Monkey([82, 66, 87, 78, 77, 92, 83], lambda x: x + 1, 11, [5, 0]),
    Monkey([97, 53, 53, 85, 58, 54], lambda x: x * 7, 13, [4, 3]),
    Monkey([50], lambda x: x + 3, 3, [1, 7]),
    Monkey([64, 69, 52, 65, 73], lambda x: x + 6, 17, [3, 7]),
    Monkey([57, 91, 65], lambda x: x + 5, 2, [0, 6]),
    Monkey([67, 91, 84, 78, 60, 69, 99, 83], lambda x: x * x, 5, [2, 4]),
    Monkey([58, 78, 69, 65], lambda x: x + 7, 19, [5, 1])
]

for _ in range(20):
    new_items = []
    for monkey in monkeys:
        new_items.extend(monkey.inspect())
    for item, monkey_id in new_items:
        monkeys[monkey_id].items.append(item)

counts = [monkey.count for monkey in monkeys]
counts.sort(reverse=True)
monkey_business = counts[0] * counts[1]
print(monkey_business)