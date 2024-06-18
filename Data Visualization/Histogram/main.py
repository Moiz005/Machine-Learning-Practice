import matplotlib.pyplot as plt

file = open('agedata.csv', 'r')
fileData = file.readlines()
ageList = []

for records in fileData:
    ageList.append(int(records))

bin = [0,10,20,30,40,50,60,70,80,90,100]

plt.title('Age Histogram')
plt.xlabel('Group')
plt.ylabel('Age')

plt.hist(ageList, bin, histtype='bar', rwidth=0.9)

plt.show()