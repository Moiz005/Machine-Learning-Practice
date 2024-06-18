import matplotlib.pyplot as plt

f = open("salesdata2.csv")
data = f.readlines()

s_data = []
c_data = []

for lines in data:
    sales, cost = lines.split(sep=",")
    s_data.append(int(sales))
    c_data.append(int(cost))

plt.title("Scatter Plot displaying sales and cost relation")
plt.xlabel("Sales")
plt.ylabel("Cost")
plt.scatter(s_data, c_data)

plt.show()