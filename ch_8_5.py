fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
l = list()
for line in fh:
    line = line.rstrip()
    if not line.startswith("From:") : continue
    try:
        words = line.split()
        x = l.append(words[1])
        print(words[1])
    except ValueError:
        pass
#print(l)
count = len(l)
print(l)
print("There were", count, "lines in the file with From as the first word")
