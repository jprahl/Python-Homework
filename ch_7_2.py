# Use the file name mbox-short.txt as the file name
#searches a txt file for X-DSPAM-Confidence: and the extracts the
#floating number that follows
fname = input("Enter file name: ")
fh = open(fname)
#confid_fh = io.StringIO("assignment7_2_confid_x_dspam")
# Use the file name mbox-short.txt as the file name
k=[]
l=[]
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    for t in line.split():
        try:
            x = l.append(float(t))
        except ValueError:
            pass
    #confid_fh.write(line)
    #print(line)
    #try:
    #    x = l.append(float(line))
    #except ValueError:
        #print(repr(line))
    #    pass
#fh.close()
#confid_fh.close()
#cnfh = open("assignment7_2_confid_x_dspam.txt")
#l = []
#for t in cnfh.read().split():
#    try:
#        x = l.append(float(t))
#    except ValueError:
       #print(repr(t))
#       pass
print(l)
total = 0
count = 0
for each in l:
    total = each + total
    count = count + 1
print(total)
average = total/count
print("Average spam confidence:",average)
#print(x)
#for t in fname.split():
#    try:
#        x = float(t)
#        break
#    except:
#        continue
#dir(fname)
#dir(fh)
#help(str.isdecimal)
#dec_1_strt = fh.find('.')
#if dec_1_strt
#print (x)
#print(x)
#for line in fh:
#    if not line.startswith("X-DSPAM-Confidence:") : continue
#    print(line)
#print("Done")
