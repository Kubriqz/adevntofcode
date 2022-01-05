list =[]

file1 = open('21.data', 'r')
Lines = file1.readlines()
print("hello")
tmp_direction = 0
count = 0
tmp_range = 0 
vertikal = 0 
horizontal = 0
for line in Lines:
    x = line.split(" ")
    if x[0] == "forward":
        horizontal += int(x[1])
    if x[0] == "up":
        vertikal -= int(x[1])
    if x[0] == "down":
        vertikal += int(x[1])
    print(x[1])

print(horizontal)
print(vertikal)
print(horizontal*vertikal)
print(len(Lines))