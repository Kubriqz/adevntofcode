#head
file1 = open('31.data', 'r')
Lines = file1.readlines()
print("aufgabe 3.1")

bitstring =""
length_of_bits = len(Lines[1])-1
#init countlist 
count = [0] * length_of_bits
#count 
for line in Lines:
    for x in range(0,length_of_bits):
        if line[x] == "1":
             count[x] += 1

print(f"list length {len(Lines)}")
#evaluate and concat string
for x in range(0,length_of_bits):
    print(count[x])
    if count[x] > len(Lines) /2:
        bitstring += "1"
    else:
        bitstring += "0"

#reverse
epsilon_string = "".join('1' if x == '0' else '0' for x in bitstring)

gamma = int(bitstring,2)
epsilon = int(epsilon_string,2)
print(f' bitstring1 is {bitstring}  gamma is {gamma}')
print(f' bitstring2 is {epsilon_string}  epsilon is {epsilon}')
print(f' power is {gamma*epsilon}')