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

finallist = listoflistoffvalid[-1]
for xyz in finallist:
    print(xyz.name)
