#head


print("aufgabe 3.1")

length_of_bits = 12
#init countlist 
count = [0] * length_of_bits
  
def get_new_list():
    file1 = open('31.data', 'r')
    Lines = file1.readlines()
    return Lines


def evaluate(x):
    if count[x] > 1000 /2 or count[x] == 500:
        return 1
    else:
        return 0

def common_bits(Lines):
#count common values
    for line in Lines:
        for x in range(0,length_of_bits):
            if line[x] == "1":
                count[x] += 1    

def sortoxigen(newlist):
    #build oxygen value 


    for x in range(0,length_of_bits):
        for line in newlist:
            print(f"{line[x]}  {evaluate(x)}")
            if int(line[x]) is not int(evaluate(x)) and  len(newlist) is not 1:
                print("POP")
                newlist.remove(line)
    return newlist


def sortco2(newlist):
    
    for x in range(0,length_of_bits):
  
        for line in newlist:
            #print(f"{line[x]}  {evaluate(x)}")
            if int(line[x]) is int(evaluate(x)) and  len(newlist) is not 1:
               # print("POP")
                newlist.remove(line)
    return newlist

tmplist = get_new_list()
common_bits(tmplist)

print(f"list new {len(tmplist)}")
oxygen = sortoxigen(tmplist)

#while len(tmplist) > 1:
 #   print("")

print(f"list oxygenlength {len(oxygen)} oxygen {oxygen[0]}")   

tmplist = get_new_list()
print(f"list new {len(tmplist)}")
#while len(tmplist) > 1:
co2 = sortco2(tmplist)

print(type(co2))
print(f"list co2length {len(co2)} oxygen {co2[0]}") 
print(int(oxygen[0],2) , int(co2[0],2))
print(int(oxygen[0],2) * int(co2[0],2))





###################################
bitstring = ""
for x in range(0,length_of_bits):

    if count[x] > len(get_new_list()) /2:
        bitstring += "1"
    else:
        bitstring += "0"
print(oxygen)
print(bitstring)
