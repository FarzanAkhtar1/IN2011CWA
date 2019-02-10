RAMSize = [4,8,16]
RAMPrice = [4*15,8*15,16*15]
HDName = ['HD','SSD','XSSSD']
HDSpeed = [120,300,420]
InputBudget = 320 #input budget
HDPrice = [39,95,250] #need to put in corresponding HD prices
pmin = 1.96 * (10 ** -6) #enter value
r = 3.8 * (10 ** -5) #enter value
Smin = 1.1 * (10 ** -4) #enter value
d = 0.39 #enter value

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
print("NOT SURE IF THIS IS WORKING PROPERLY \n")
for ramprice in RAMPrice:
    placeholder = 0
    for hdprice in HDPrice:
        Budget = InputBudget
        Budget = Budget - hdprice - ramprice
        if Budget >= 0:
            print("RAM size " + str(ramprice/15) + "GiB and HD is " + str(HDName[placeholder]) + " and total cost is: £" + str((hdprice + ramprice)))
            p = pmin + r/(ramprice/15)
            s = Smin + d/(HDSpeed[placeholder])
            print(p)
            print(s)
            print("EAT is: "+ str(round(((1-p)*200) + (p * s),3)) + " nanoseconds")
            print("")
            
        placeholder = placeholder + 1


print("\n")
print("---Question 3---\n")
print("I hope this is right, no promises")
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
            outNumber = format(-(((((1-p)*200) + (p * s))-200)/200)*100, "10.2E")
            outNumbers.append(outNumber)
            #print(str(outNumber) + "%")
            #print("")
            
        placeholder = placeholder + 1          
#print(outStrings)
#print(outNumbers)
minIndex = outNumbers.index(min(outNumbers))
maxIndex = outNumbers.index(max(outNumbers))
print("Lowest degradation is for: " + outStrings[minIndex] + " with degradation of " + outNumbers[minIndex] + "%")
print("Highest degradation is for: " + outStrings[maxIndex] + " with degradation of " + outNumbers[maxIndex] + "%")
