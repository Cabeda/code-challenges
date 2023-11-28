import pandas as pd

def alergenios 
alergenios = []
alergenios_compostos = []
with open("data.txt", "r") as f:
    for line in f.readlines():
        line = line.strip().lower()
        alergenios_compostos.append(line)
        if len(line) > 0:
            items = [item.strip() for item in line.split("+")]
            alergenios = alergenios + items

alergenios = pd.DataFrame(alergenios, columns=["Alergenio"])
alergenios_compostos = pd.DataFrame(alergenios_compostos, columns=["Alergenio"])

print(alergenios.groupby("Alergenio").size())
print(alergenios_compostos.groupby("Alergenio").size())