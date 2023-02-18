from keras.models import Sequential
from keras.layers import Dense
import numpy as np

#crear modelo
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
#Cargar pesos del modelo
model.load_weights("checkpoint/weights-best.hdf5")
#COMPILE MODEL
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print("Modelos creado con pesos del fichero")
#Posteriormente cargamos los datos ,separamos y evaluamos con el modelo ya cargado con los pesos.
dataset = np.loadtxt("C:/dev/generadorPython/Datasets/pima-indians-diabetes.csv", delimiter=',')
X = dataset[:, 0:8]
y = dataset[:, 8]
#Estimación de valores accuracy del dataset con los pesos cargados
scores=model.evaluate(X,y,verbose=0)
print("%s: %.2f%%" %(model.metrics_names[1],scores[1]*100))
