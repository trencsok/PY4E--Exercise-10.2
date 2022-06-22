name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
    #line = line.rstrip()
    if line.startswith("From "):
        address = line.split()
        #print(address)
        x = line.find(":")
        hour = line[x-2:x]
        #print(hour)
        counts[hour] = counts.get(hour,0) + 1

lst = list()
for key, val in list(counts.items()):
    lst.append((key,val))
#print(lst)
lst.sort()
#print(lst)
for key,val in lst:
    print(key,val)
