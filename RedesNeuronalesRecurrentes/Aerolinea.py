import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv("C:\dev\generadorPython\Datasets\international-airline-passengers.csv",usecols=[1],engine='python')
plt.plot(dataset)
plt.show()
print(dataset)
#Usaremos estos datos en un Multilayer Percetron MLP para regresión
