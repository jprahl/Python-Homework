userfile = input("Which file would you like to read in all caps?")
try:
    txt_file_1 = open(userfile)
#    print(txt_file_1)
#
#    pass
except:
    print('I canna do it Jim...not',userfile)
    exit()
# count = 0
# for line in txt_file_1:
    #count = count + 1
# print('LineCount:',count)

red_txt_file_1 = txt_file_1.read()
#print('Length:',len(red_txt_file_1))
print(red_txt_file_1.upper().strip())
#print(txt_file_1)
