import matplotlib.pyplot as plt

f = open("salesdata.csv")
data = f.readlines()

salesData = []
for line in data:
    salesData.append(int(line))

plt.title("Box PLot for sales data")
plt.boxplot(salesData, showfliers=False)
plt.show()