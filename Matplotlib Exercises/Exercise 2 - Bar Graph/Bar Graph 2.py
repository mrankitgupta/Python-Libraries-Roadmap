from matplotlib import pyplot as plt

players = ['Ankit', 'Dhoni', 'Rohit','Shikhar']
runs = [51,87,45,67]
plt.barh(players,runs, color = 'green')
plt.title('Score Card')
plt.xlabel('Players')
plt.ylabel('Runs')
plt.show()