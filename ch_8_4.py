#reads in a txt file, and arrannges words in alphabetical order (caps first)
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    for word in line.split():
        try:
            if word in lst : continue
            w = lst.append(word)
        except ValueError:
            pass
lst.sort()
print(lst)
