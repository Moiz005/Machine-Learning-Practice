import matplotlib.pyplot as plt
# x_cities = ['New York', 'London', 'Dubai', 'New Delhi', 'Tokyo']
x_cities = [1, 2, 3, 4, 5]
y_temp = [75, 65, 105, 98, 90]
y_temp1 = [50, 80, 105, 40, 57]
plt.title("Temperature Variations")
plt.xlabel("Cities")
plt.ylabel("Temperature")

plt.plot(x_cities, y_temp, label = "Temp1")
plt.plot(x_cities, y_temp1, label = "Temp2")

plt.legend(loc=2, fontsize=15)
plt.show()