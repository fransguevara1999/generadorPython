# Guardar en YAML
"""
Guardar como model.foresYML , luego cargar el modelo a través de la funcion model_from_yaml().
Los pesos se siguen guardando en HDF5, model.h5
"""
import os.path

from keras.models import Sequential
from keras.layers import Dense
#from keras.models import model_from_yaml
import ruamel.yaml
import numpy as np

# cargar conjunto de datos
dataset = np.loadtxt("C:/dev/generadorPython/Datasets/pima-indians-diabetes.csv", delimiter=',')
X = dataset[:, 0:8]
y = dataset[:, 8]
# salida
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# compilar
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# evaluación
model.fit(X, y, epochs=150, batch_size=10, verbose=0)
scores = model.evaluate(X, y, verbose=0)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))
# Serialize model to YML
ruta = os.path.expanduser("C:/dev/generadorPython/Redes Neuronales Avanzados/foresYML/model.yaml")
model_yaml = model.to_yaml()
with open(ruta, "w") as yaml_file:
    yaml_file.write(model_yaml)

model.save_weights("model.h5")
print("Modelo guardado")
