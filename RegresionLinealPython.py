# Clasificación Binaria

import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# Caragar datos
dataframe = pd.read_csv("Datasets/housing.csv", delim_whitespace=True, header=None)
dataset = dataframe.values
# print(dataset)
X = dataset[:, 0:13]
y = dataset[:, 13]


# print("Valor X:")
# print(X)
# print("Valor Y:")
# print(y)

def baseline_model():
    # creación Modelo
    model = Sequential()
    model.add(Dense(13, input_dim=13, activation="relu"))
    model.add(Dense(1))
    # Compilación
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model


# Agregar más capas (más profunda)
def larger_model():
    # creación Modelo
    model = Sequential()
    model.add(Dense(13, input_dim=13, activation="relu"))
    model.add(Dense(6, activation="relu"))
    model.add(Dense(1))
    # Compilación
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

#Agregando más neuronas
def topologia_grande():
    # creación Modelo
    model = Sequential()
    model.add(Dense(20, input_dim=13, activation="relu"))
    model.add(Dense(1))
    # Compilación
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model


estimador = KerasRegressor(build_fn=baseline_model, epochs=100, batch_size=5, verbose=0)
kfold = KFold(n_splits=10)
result = cross_val_score(estimador, X, y, cv=kfold)
print("Linea base: %.2f (%.2f) MSE" % (result.mean(), result.std()))

# optimizar con procesamiento de datos...
estimadores = []
estimadores.append(('standarize', StandardScaler()))
estimadores.append(('topologia-NN', KerasRegressor(build_fn=baseline_model, epochs=100, batch_size=5, verbose=0)))
pipeline = Pipeline(estimadores)
kfold = KFold(n_splits=10)
result = cross_val_score(pipeline, X, y, cv=kfold)
print("topologia-NN: %.2f (%.2f) MSE" % (result.mean(), result.std()))
