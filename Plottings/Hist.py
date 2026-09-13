#Plot Histogram in matplotlib

import matplotlib.pyplot as plt
import numpy as np

arr = np.array([10,20,30,40,50,60,70,80,80,11,22,33,44,55,66,12,13,14,56])

plt.hist(arr,bins=[0,10,20,30,40,50,60,70,80,90])

plt.xlabel("Marks")
plt.ylabel("Students")

plt.title("Students Marksheet")
plt.show()
