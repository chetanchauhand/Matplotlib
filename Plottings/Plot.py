import pandas as pd
import matplotlib.pyplot as plt

data ={
    "Temp" : [50,40,44,44,45,42,23,20,12],
    "Humidity" : [20,12,13,11,20,34,5,12,3],
    "Wind" : [2,3,4,5,6,7,8,12,10],
    "Precipitation" : [9,8,7,6,4,5,2,3,1]
}

df = pd.DataFrame(data)

# df.plot()

df["Temp"].plot(kind='hist')

plt.show()