import matplotlib.pyplot as plt

f = open("salesdata2.csv")
data = f.readlines()

s_data = []
c_data = []

for lines in data:
    sales, cost = lines.split(sep=",")
    s_data.append(int(sales))
    c_data.append(int(cost))


f.close()


f = open("salesdata.csv")
data = f.readlines()

salesData = []
for line in data:
    salesData.append(int(line))

# plt.figure("My Scatter Plot")  # For plotiing the graph in a different figure
plt.subplot(2,1,1)
plt.title("Scatter Plot displaying sales and cost relation")
plt.xlabel("Sales")
plt.ylabel("Cost")
plt.scatter(s_data, c_data)


# plt.figure("My Box Plot")  # For plotiing the graph in a different figure
plt.subplot(2,1,2)
plt.title("Box PLot for sales data")
plt.boxplot(salesData, showfliers=False)

plt.tight_layout()
plt.show()