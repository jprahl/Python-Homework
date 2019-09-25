largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        fnum = float(num)
    except:
        print("Invalid input")
    #print(num)
    if largest is None or fnum > largest :
        largest = int(fnum)
    #elif fnum > largest :
        #largest = int(fnum)
        continue
    if smallest is None or fnum < smallest :
        smallest = int(fnum)
    #elif fnum < smallest :
        #smallest = int(fnum)
        continue
print("Maximum is", largest)
print("Minimum is", smallest)
