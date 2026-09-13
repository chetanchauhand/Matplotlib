#Pie chart

import matplotlib.pyplot as plt
import numpy as np

Cricketer = np.array(["Kl.Rahul","Surya","Virat","Ms.Dhoni","Rohit"])
Runs = np.array([70,75,60,90,55])

plt.pie(Runs,labels=Cricketer,autopct='%1.3f%%')

plt.title("Runs scored in match")

plt.show()