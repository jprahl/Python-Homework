# 9.4 Write a program to read through the mbox-short.txt and
# figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of
# those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's
#  mail address to a count of the number of times they appear in
# the file. After the dictionary is produced, the program reads
# through the dictionary using a maximum loop to find the most
# prolific committer.
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
l = list()# List of names
l_n = list()# list of times
l_h = list()# list of hours
for line in fh:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    time = words[5] # There really has to be a better way to identify the time
    hr_min_s = time.split(':')
    hours = hr_min_s[0]
    try:
        x = l_n.append(time)
        h = l_h.append(hours)
        #print(time)
        #print(hours)
        #print(words[1])
#        try:
#            times = line.split(':',1)
#            x = l_n.append(times[0]) if times.isdigit()
#        except ValueError:
#            pass
    except ValueError:
        pass
#print(l)
counts = dict()
#for email in l :
#    counts[email] = counts.get(email,0)+1
for hours in l_h :
    counts[hours] = counts.get(hours,0)+1
#count = len(l)
most_occurances = None
new_most = None
times_sorted = list()
#for email,occurances in counts.items() :
#    if most_occurances is None or occurances > most_occurances:
#        new_most = email
#        most_occurances = occurances
    #print(email,occurances)
#print(new_most,most_occurances)
#print(l)
#print(l_h)
#print(l)
for h,occ in counts.items() :
    times_sorted.append((h,occ))
#print(counts)
times_sorted.sort()
for h,occ in times_sorted :
    print (h,occ)
#print(times_sorted)
#print(counts.values())
