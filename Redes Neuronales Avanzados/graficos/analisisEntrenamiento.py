#Visualización de historial de entrenamiento
import keras.losses
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
import numpy as np

#Cargar datos
dataset=np.loadtxt("C:/dev/generadorPython/Datasets/pima-indians-diabetes.csv",delimiter=",")
#Partición
X=dataset[:, 0:8]
y=dataset[:, 8]
#Creamos modelo
model=Sequential()
model.add(Dense(12,input_dim=8,activation='relu'))
model.add(Dense(8,activation='relu'))
model.add(Dense(1,activation='sigmoid'))
#Compilar modelo
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
#Ajustar el modelo
history=model.fit(X,y,validation_split=0.33,epochs=150,batch_size=10,verbose=0)
#imprimir historial
print((history.history.keys()))
#Representar la metrica para el accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title("Accuracy del modelo")
plt.ylabel("Accuracy")
plt.xlabel("Epoch")
plt.legend(['entrenamiento', 'validacion'],loc='upper left')
plt.show()

#Representar la metrica para el accuracy
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title("Loss del modelo")
plt.ylabel("Loss")
plt.xlabel("Epoch")
plt.legend(['entrenamiento', 'validacion'],loc='upper left')
plt.show()