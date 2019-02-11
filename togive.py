#In your team's parameter file where you have values such as 1.96E-6. The E-6 refers to (10 ** -6)
#So you will need to change the -6 to reflect a difference in your paramters


#----------------------------------------------------
#ENTER GROUP PARAMETERS HERE

InputBudget = 320 #input budget
HDPrice = [39,95,250] #need to put in corresponding HD prices in the order of: HD, SSD then XSSSD
pmin = 1.96 * (10 ** -6) #enter value
r = 3.8 * (10 ** -5) #enter value
Smin = 1.1 * (10 ** -4) #enter value
d = 0.39 #enter value

#YOU WON'T HAVE TO CHANGE ANYTHING BELOW THIS LINE
#----------------------------------------------------

RAMSize = [4,8,16]
RAMPrice = [4*15,8*15,16*15]
HDName = ['HD','SSD','XSSSD']
HDSpeed = [120,300,420]


print("---Question 1---\n")
for ramprice in RAMPrice:
    placeholder = 0
    for hdprice in HDPrice:
        Budget = InputBudget
        Budget = Budget - hdprice - ramprice
        if Budget >= 0:
            print("RAM size " + str(ramprice/15) + "GiB and HD is " + str(HDName[placeholder]) + " and total cost is: £" + str((hdprice + ramprice)))
        placeholder = placeholder + 1

print("\n")
print("---Question 2---\n")
for ramprice in RAMPrice:
    placeholder = 0
    for hdprice in HDPrice:
        Budget = InputBudget
        Budget = Budget - hdprice - ramprice
        if Budget >= 0:
            print("RAM size " + str(ramprice/15) + "GiB and HD is " + str(HDName[placeholder]) + " and total cost is: £" + str((hdprice + ramprice)))
            p = float(pmin + r/(ramprice/15))
            s = float(Smin + d/(HDSpeed[placeholder]))
            #print(p)
            #print(s)
            #print((1-p)*200 + (p*s))
            print("Effective Access Time is: "+ str(format(float((200*(10 ** -9)) + (p*s)), "10.2E") + " seconds"))
            print("")
            
        placeholder = placeholder + 1


print("---Question 3---\n")
#print("I hope this is right, no promises")
outStrings = []
outNumbers = []
for ramprice in RAMPrice:
    placeholder = 0
    for hdprice in HDPrice:
        Budget = InputBudget
        Budget = Budget - hdprice - ramprice
        if Budget >= 0:
            outString = "RAM size " + str(ramprice/15) + "GiB and HD is " + str(HDName[placeholder])
            outStrings.append(outString)
            #print(outString)
            p = pmin + r/(ramprice/15)
            s = Smin + d/(HDSpeed[placeholder])
            EAT = (200*(10 ** -9)) + (p*s)
            BAT = 200*(10 ** -9)
            outNumber = float( (EAT - BAT) / BAT )
            #print(outNumber)
            outNumbers.append(outNumber)
            #print(str(outNumber) + "%")
            #print("")
            
        placeholder = placeholder + 1          
#print(outStrings)
#print(outNumbers)
minIndex = outNumbers.index(min(outNumbers))
maxIndex = outNumbers.index(max(outNumbers))
#print(minIndex)
#print(maxIndex)
print("Lowest degradation is for: " + outStrings[minIndex] + " with degradation of" + format(outNumbers[minIndex],"10.2E") + "%")
print("Highest degradation is for: " + outStrings[maxIndex] + " with degradation of" + format(outNumbers[maxIndex], "10.2E") + "%")
