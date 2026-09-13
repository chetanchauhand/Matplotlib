import matplotlib.pyplot as plt
import numpy as np

student = np.array(["Raj","Guru","Arsh","jahan","Kabir"])
Marks = np.array([80,81,82,90,91])

plt.bar(student,Marks)

plt.xlabel("student")
plt.ylabel("Marks")

plt.title("Student Mathmatics Performance:")
plt.show()