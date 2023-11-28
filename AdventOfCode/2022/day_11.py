from enum import Enum


class Type(Enum):
    Monkey = "Monkey"
    items = "Starting items"
    operation = "Operation"
    test = "Test"
    true = "If true"
    false = "If false"


class Math(Enum):
    mul = "*"
    add = "+"
    min = "-"
    div = "/"


class Monkey:

    num: int
    items = str
    operation: str
    test: str
    true: str
    false: str

    def __str__(self):
        print(f"num: {self.num}")
        print(f"items: {self.items}")
        print(f"operation: {self.operation}")
        print(f"test: {self.test}")
        print(f"true: {self.true}")
        print(f"false: {self.false}")


monkeys = []

with open("input_11.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        print(line)

        # Nothing to do
        if len(line) == 0:
            continue

        [op, info] = line.split(":")
        match op:
            case Type.Monkey.items.value:
                monkeys[-1].items = [int(item.strip()) for item in info.split(",")]
            case Type.Monkey.operation.value:
                monkeys[-1].operation = info
            case Type.Monkey.test.value:
                monkeys[-1].test = info
            case Type.Monkey.true.value:
                monkeys[-1].true = info
            case Type.Monkey.false.value:
                monkeys[-1].false = info
            case _:
                monkey = Monkey()
                monkey.num = len(monkeys)
                monkeys.append(Monkey())


num_cycles = 20

print("Starting cycles")
for cycle in range(0, num_cycles):
    print(cycle)
    for monkey in monkeys:
        print(f"{monkey}")
