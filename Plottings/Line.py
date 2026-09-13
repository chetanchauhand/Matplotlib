#Line Chart

import matplotlib.pyplot as plt
import numpy as np

Month = np.array(["Jan","Feb","Mar","Apr","May","June","July","Aug","Sep","Auc","Nov","Dec"])
Rain = np.array([20,22,40,50,60,54,59,80,88,90,99,10])

plt.plot(Month,Rain)

plt.xlabel("Months")
plt.ylabel("Rainfall (mm)")

plt.title("RainFall in an year")

plt.show()