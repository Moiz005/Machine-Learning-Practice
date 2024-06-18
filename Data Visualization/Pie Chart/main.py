import matplotlib.pyplot as plt
from collections import Counter

f = open("agedata2.csv")

data = f.readlines()
city_list = []

for lines in data:
    age,city = lines.split(sep=",")
    city_list.append(city)

city_count = Counter(city_list)
city_names = city_count.keys()
city_values = city_count.values()

plt.title("Pie Chart for City")
plt.pie(city_values, labels=city_names, autopct='%.2f%%')
plt.show()