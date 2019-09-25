#The basic outline of this problem is to read the file,
# look for integers using the re.findall(),
#looking for a regular expression of '[0-9]+'
#and then converting the extracted strings to integers and summing
# up the integers.
import re#load regular exressions
fbr = open('regex_sum_252643.txt')#file being read
num_lst = list()
for line in fbr:
    line = line.rstrip()#why remove the white space again?
    try:
        x = re.findall('[0-9]+',line)
        if len(x) > 0: num_lst.extend(x)
    except ValueError:
        pass
#flat_list = []
#for sublist in num_lst: #simplify to a single list instead of a list of lists
#    for item in sublist:
#        flat_list.append(item)
for i in range(0,len(num_lst)):
    num_lst[i] = int(num_lst[i])
#print(num_lst)
#print(flat_list)
#print(sum(num_lst))
#Additional exercise - can be done in 2 lines:
#Python 3:
print(sum([int(i) for i in re.findall('[0-9]+',open('regex_sum_252643.txt').read())]))
#print(sum(map(int, re.findall(r'\d+',open('regex_sum_252643.txt').read()))))
