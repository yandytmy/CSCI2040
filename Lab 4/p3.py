#python_version == '3.7'

import matplotlib.pyplot as plt
import numpy as np

plt.figure(1)
random_numbers = np.random.normal(0, 1, 1000)
plt.title("Histogram - Probability Density of Random Numbers")
plt.xlabel("Value of Random Number")
plt.ylabel("Probability Density")
plt.hist(random_numbers)
plt.savefig("histogram.png")

plt.figure(2)
plt.title("Pie Chart - Precentage of students of 3 selected colleges in CUHK in 2019")
labels = 'Morningside College', 'S.H. Ho College', 'Wu Yee Sun College' 
sizes = [300, 600, 1258]
plt.pie(sizes, labels = labels, autopct = '%1.1f%%', startangle = 0)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.savefig("pie.png")

plt.figure(3)
plt.title("Bar Chart - Number of students of all 9 colleges in CUHK in 2019")
College = 'Chung Chi College', 'New Asia College', 'United College', 'Shaw College',  'Morningside College', 'S.H. Ho College', 'CW Chu College', 'Wu Yee Sun College', 'Lee Woo Sing College'
Number = [3193, 3424, 3324, 3595, 300, 600, 300, 1258, 1322]
plt.bar(College, Number)
plt.xticks(College, rotation = 45, horizontalalignment = "right")
plt.xlabel("College")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("bar.png")

plt.figure(4)
plt.title("Scatter plot & line chart - Relationship between two continuous variables")
x_list = np.linspace(0, 1, 100)
y_list = x_list + np.random.rand(100)
plt.plot(x_list, x_list, linestyle = "dashed")
plt.scatter(x_list, y_list, marker = "*", color = "red")
plt.xlabel("x_list")
plt.ylabel("y_list")
plt.savefig("scatter_line.png")
