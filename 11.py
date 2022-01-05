list =[]

file1 = open('11.data', 'r')
Lines = file1.readlines()
print("11")
tmp = 0
count =0
for line in Lines:
    
    if int(tmp) < int(line):
        count +=1
    tmp=line    
print(count)
print(len(Lines))