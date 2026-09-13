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

res = ag.legend(loc = 'upper center',fontsize = 'xx-large')
res.get_frame().set_facecolor('red')
plt.title("Frequency of signal is:")

plt.show()



