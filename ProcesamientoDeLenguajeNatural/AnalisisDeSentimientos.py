import numpy as np
from keras.datasets import imdb
import matplotlib.pyplot as plt

#Cargar Datos
(X_train,y_train),(X_test,y_test)=imdb.load_data()
X=np.concatenate((X_train,X_test),axis=0)
y=np.concatenate((y_train,y_test),axis=0)
#Numero de clases
#print(np.unique(y))
#Palabras unicas en el conjunto de datos
#print(len(np.unique(np.hstack(X))))
#Tamaño medio de la reseña
result=[len(x) for x in X]
print("Media de palabras: %.2f (%f)" % (np.mean(result), np.std(result)))
#media de cada una de las palabras
#Graficar
plt.subplot(121)
plt.boxplot(result)
plt.subplot(122)
plt.hist(result)
plt.show()


