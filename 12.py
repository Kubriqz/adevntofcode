list =[]

file1 = open('11.data', 'r')
Lines = file1.readlines()
print("hello")
tmp = 0
count = 0
tmpalt = 0 

for x in range(0, len(Lines)):
    tmp = int(Lines[x])+int(Lines[x+1])+int(Lines[x+2])

    if int(tmp) > int(tmpalt):
        count +=1
    tmpalt = tmp

print(count)
print(len(Lines))