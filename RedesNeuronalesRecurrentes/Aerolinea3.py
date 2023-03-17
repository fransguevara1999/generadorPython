import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from keras.models import Sequential
from keras.layers import Dense

dataframe = pd.read_csv("C:\dev\generadorPython\Datasets\international-airline-passengers.csv", usecols=[1],
                        engine='python')
dataset = dataframe.values
dataset = dataset.astype('float32')
print(dataset)
# Entrenamiento y validacion
train_size = int(len(dataset) * 0.67)
test_set = len(dataset) - train_size
train, test = dataset[0:train_size, :], dataset[train_size:len(dataset), :]
print(train)
print(test)


# plt.plot(dataset)
# plt.show()
# Usaremos estos datos en un Multilayer Percetron MLP para regresión
# Crear arreglo antes y despues en base a nustros datos
def create_dataset(dataset, loock_back=1):
    dataX, dataY = [], []
    for i in range(len(dataset) - loock_back - 1):
        a = dataset[i:(i + loock_back), 0]
        dataX.append(a)
        dataY.append(dataset[i + loock_back, 0])
    return np.array(dataX), np.array(dataY)


look_back = 1
trainX, trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test, look_back)
for i in range(5):
    print(trainX[i], trainY[i])

# Crear modelo sequencial
model = Sequential()
model.add(Dense(8, input_dim=look_back, activation='relu'))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(trainX, trainY, epochs=200, batch_size=2, verbose=2)

# Estimar modelo
trainScore = model.evaluate(trainX, trainY, verbose=0)
print('Puntuacion Entrenamiento: %.2f MSE (%.2f RMSE)' % (trainScore, math.sqrt(trainScore)))
testScore = model.evaluate(testX, testY, verbose=0)
print('Puntuacion Validacion: %.2f MSE (%.2f RMSE)' % (testScore, math.sqrt(testScore)))

# Predicciones del modelo
tranPredict = model.predict(trainX)
testPredict = model.predict(testX)

trainPredictPlot = np.empty_like(dataset)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back: len(tranPredict) + look_back, :] = tranPredict

testPredictPlot = np.empty_like(dataset)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(tranPredict) + (look_back*2) + 1 : len(dataset)-1,: ] = testPredict

plt.figure(figsize=(12,8))
plt.plot(dataset)
plt.plot(trainPredictPlot)
plt.plot(testPredictPlot)
plt.show()