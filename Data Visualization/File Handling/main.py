cityTemp = open("citytemp.csv", "r")
prevCity = ""
data = cityTemp.readlines()
tempData = []
writeData = []
avgTemp = 0
count = 0
for dataLine in data:
    dataLine = dataLine.rstrip('\n')
    dataLine = dataLine.split(",")
    tempData.append(dataLine)
# print(tempData)
for dataLine in tempData:
    temp = float(dataLine[1])
    if dataLine[2] == "C":
        temp = (temp * (9 / 5)) + 32
        dataLine[2] = "F"
    if prevCity == "":
        prevCity = dataLine[0]
        count += 1
        avgTemp += temp
    elif prevCity == dataLine[0]:
        count += 1
        avgTemp += temp
    else:
        avgTemp = avgTemp/count
        writeData.append(prevCity + "," + str(avgTemp) + "," + "F")
        avgTemp = temp
        count = 1
        prevCity = dataLine[0]
else:
    avgTemp = avgTemp / count
    writeData.append(prevCity + "," + str(avgTemp) + "," + "F")
print(tempData)