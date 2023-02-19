import pandas as pd
import math as mth
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
from sklearn.preprocessing import LabelEncoder
from keras.callbacks import LearningRateScheduler
import matplotlib.pyplot as plt

#Planificador de tasa de aprendizaje
def step_decay(epoch):
    initial_lrate=0.1
    drop=0.5
    epochs_drop=10
    lrate=initial_lrate*mth.pow(drop,mth.floor(1+epoch)/epochs_drop)
    return lrate

df = pd.read_csv("C:/dev/generadorPython/Datasets/ionosphere.csv", header=None)
df_values = df.values
X = df_values[:, 0:34].astype(float)
y = df_values[:, 34]

encoder = LabelEncoder()
encoder.fit(y)
y_encoder = encoder.transform(y)

model = Sequential()
model.add(Dense(34, input_dim=34, activation='relu'))
model.add(Dense(1, activation='sigmoid'))


sgd = SGD(learning_rate=0.0, momentum=0.9)
model.compile(loss='binary_crossentropy', optimizer=sgd, metrics=['accuracy'])

#Planificador de aprendizaje
lrate=LearningRateScheduler(step_decay)
callback_list=[lrate]

history=model.fit(X, y_encoder, validation_split=0.33, epochs=50, batch_size=28,callbacks=callback_list ,verbose=2)
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