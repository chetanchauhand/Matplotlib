import matplotlib.pyplot as plt
import numpy as np

team1_Score = np.array([7,13,33,44,47,49,66])
team2_Score = np.array([5,12,14,19,55,59,67])

Score_Range = np.array([5,10,15,20,25,30,35])

plt.scatter(team1_Score, Score_Range ,colorizer='r')

plt.scatter(team2_Score,Score_Range ,colorizer='b' )

plt.xlabel("Team Score")
plt.ylabel("Score Range")

plt.title("Score of two team")

plt.show()