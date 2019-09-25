# 9.4 Write a program to read through the mbox-short.txt and
# figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of
# those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's
#  mail address to a count of the number of times they appear in
# the file. After the dictionary is produced, the program reads
# through the dictionary using a maximum loop to find the most
# prolific committer.


#Use this same method to solve the "Mississippi" to iiiissssppM problem

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
        #print(words[1])
    except ValueError:
        pass
#print(l)
counts = dict()
for email in l :
    counts[email] = counts.get(email,0)+1
#count = len(l)
most_occurances = None
new_most = None
for email,occurances in counts.items() :
    if most_occurances is None or occurances > most_occurances:
        new_most = email
        most_occurances = occurances
    #print(email,occurances)
print(new_most,most_occurances)
print(l)
#print(l)
#print(counts)
#print(counts.values())
