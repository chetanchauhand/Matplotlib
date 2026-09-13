# Add legend in graph with matplotlib

import matplotlib.pyplot as plt
import numpy as np

a = np.arange(6)
b = np.array([10,20,30,40,50,60])
c = np.array([11,22,33,44,55,66])

#Create plot
fg = plt.figure()
ag = plt.subplot()

ag.plot(a,b,'k--',label='frequency')
ag.plot(a,c,'k:',label = 'Periods')

# ag.legend()
ag.legend(loc = 'lower center')

plt.title("Frequency of signal:\n",loc='right')

plt.show()
