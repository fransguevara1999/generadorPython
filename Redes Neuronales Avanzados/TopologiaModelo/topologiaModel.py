from keras.models import Sequential
from keras.layers import Dense
from keras.models import load_model
import numpy as np

#cargar conjunto de datos
dataset=np.loadtxt("C:/dev/generadorPython/Datasets/pima-indians-diabetes.csv",delimiter=',')
X=dataset[:,0:8]
y=dataset[:,8]
#salida
model=Sequential()
model.add(Dense(12,input_dim=8,activation='relu'))
model.add(Dense(8,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

#compilar
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

#compilar
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

#evaluación
model.fit(X,y,epochs=150,batch_size=10,verbose=0)

scores=model.evaluate(X,y,verbose=0)
print("%s: %.2f%%" % (model.metrics_names[1],scores[1]*100))
#Guardar modelo
model.save("model.h5")
print("Modelo guardado")
#=================CARGAR MODELO========================
#Cargar modelo
model=load_model("model.h5")
model.summary()

#Cargar data set
dataset=np.loadtxt("C:/dev/generadorPython/Datasets/pima-indians-diabetes.csv",delimiter=',')
X=dataset[:,0:8]
y=dataset[:,8]
#Evaluacion
scores=model.evaluate(X,y,verbose=0)
print("%s: %.2f%%" % (model.metrics_names[1],scores[1]*100))