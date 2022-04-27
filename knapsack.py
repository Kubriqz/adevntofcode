from itertools import permutations
maxg = 15


class itemClass:
    def __init__(self, gewicht, wert, name):
        self.gewicht = gewicht
        self.wert = wert
        self.name = name


green = itemClass(12, 4, "green")
blue = itemClass(2, 2, "blue")
grey = itemClass(1, 2, "grey")
red = itemClass(1, 1, "red")
yellow = itemClass(4, 10, "yellow")


# try everything


listofitems = []

listofitems.append(green)
listofitems.append(blue)
listofitems.append(grey)
listofitems.append(red)
listofitems.append(yellow)

# itertools

perm = permutations(listofitems)
anotherlistofobjects = []

listoflistoffvalid = []

for item in list(perm):
    listofvalid = []
    gewicht = 0
    for i in item:
        if isinstance(i, itemClass):
            if gewicht + i.gewicht <= 15:
                gewicht += i.gewicht
                listofvalid.append(i)
                print(i.name)

    listoflistoffvalid.append(listofvalid)

print(":.....:")

for listofvalid in listoflistoffvalid:
    value = 0
    gewicht = 0
    for item in listofvalid:
        value += item.wert
        gewicht += item.gewicht
    print("value " + str(value))
    print("gewicht " + str(gewicht))


print()

# need wrapper object for indexing and validate


class listholderclass:
    gesamtgewicht = 0
    gesamtwert = 0

    def __init__(self, listofitems, index):

        self.listofitems = listofitems
        self.index = index  # justforfun

    def validate(self):
        for item in self.listofitems:
            self.gesamtgewicht += item.gewicht
            self.gesamtwert += item.wert


# make finallist
finallist = []
countit = 0
for listofitems in listoflistoffvalid:
    temp = listholderclass(listofitems, countit)
    temp.validate()
    finallist.append(temp)
    countit += 1

# order it
finallist.sort(key=lambda x: x.gesamtwert, reverse=True)

# take the first
for item in finallist[0].listofitems:
    print(item.name)
