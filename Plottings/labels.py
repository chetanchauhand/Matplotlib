# Add labels to a plot with matplotlib 

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Cricket Bat" : ["CEAT","MRF","HERO","SG","SS","Gray Nicolus"],
    "Price" : [1100,2000,2100,1200,1500,3400],
    "Weight_Kg" : [1,1.1,1.2,1.1,1.5,1.4]

}

df = pd.DataFrame(data)

plt.plot(df["Cricket Bat"],df["Price"])

plt.xlabel("Bat Price (USD)")
plt.ylabel("Bat Weight (Kg)")
plt.title("Bat Price depend on weight",loc="left")

plt.show()