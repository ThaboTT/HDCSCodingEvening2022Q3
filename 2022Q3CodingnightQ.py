#Function to extract string details
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
    if rstr[1] in rstr[2:]:
        secc = "@ index " + str(rstr[2:].index(rstr[1])+2)
    else:
        secc = "not found"

    #Display contents on screen
    sentdetails = """allAboutStrings("{}") -> [{}, {}", "{}", "{}", "{}"].""".format(rstr, sl, rstr[0], rstr[-1], ist, secc)
    print(sentdetails)


#To test the function
teststring = "Thabo"
teststring2 = "Ncubec"
stringdetail(teststring)
stringdetail(teststring2)
