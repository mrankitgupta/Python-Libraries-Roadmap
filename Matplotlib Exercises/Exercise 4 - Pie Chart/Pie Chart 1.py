from matplotlib import pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
Players = 'Ankit', 'Dhoni', 'Rohit', 'Yuvraj'
Runs = [25, 30, 15, 10]
explode = (0, 0.1, 0, 0)  # it "explode" the 2nd slice
fig1, ax1 = plt.subplots()
ax1.pie(Runs, explode=explode, labels=Players, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()