from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
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

#evaluación
model.fit(X,y,epochs=150,batch_size=10,verbose=0)
scores=model.evaluate(X,y,verbose=0)
print("%s: %.2f%%" % (model.metrics_names[1],scores[1]*100))
#Gurdar modelo compilado y entrenado
#Serialize model to JSON
model_json=model.to_json()
with open("model.json","w") as json_file:
    json_file.write(model_json)
#Guardar pesos en HDF5
model.save_weights("model.h5")
print("Modelo Guardado")

#Cargar modelo
json_file=open('model.json','r')
loaded_model_json=json_file.read()
json_file.close()
loaded_model=model_from_json(loaded_model_json)

loaded_model.compile(loss='binary_crossentropy',optimizer='rmsprop',metrics=['accuracy'])
print("Modelo cargado")
#Evaluación del modelo
scores=model.evaluate(X,y,verbose=0)
print("%s: %.2f%%" % (model.metrics_names[1],scores[1]*100))

