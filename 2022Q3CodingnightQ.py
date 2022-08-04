#Function extract string details
def stringdetail(rstr):
    
    sl = len(rstr) #string length

    ist = ""        #middle character variable

    #To check if the string is even or odd
    if  sl%2 == 0:  
            ist = rstr[int(sl/2)] + rstr[int((sl/2)+1)]
    else:
            ist = rstr[int((sl-1)/2)]

    secc =""    #identical index phrase variable
    
    #to check if there's an identical character as that of the second index
    if rstr[1] == rstr[2:].find(rstr[1]):
        secc = "@ index " + rstr[2:].index(rstr[1])
    else:
        secc = """not found"""

    print("allAboutStrings(" + str(rstr) + ") -> " + "[" + str(rstr[0]) + ", " + str(rstr[-1] + ", " + str(ist) + ", " + str(secc) + "]"))


teststring = "Thabo"
teststring2 = "Ncubes"
stringdetail(teststring)
stringdetail(teststring2)
