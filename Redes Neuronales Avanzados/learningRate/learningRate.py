import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
from sklearn.preprocessing import LabelEncoder

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

epochs = 50
lr = 0.1
decay_rate = lr / epochs
momento = 0.8
sgd = SGD(learning_rate=lr, momentum=momento, decay=decay_rate, nesterov=False)
model.compile(loss='binary_crossentropy', optimizer=sgd, metrics=['accuracy'])
model.fit(X, y_encoder, validation_split=0.33, epochs=epochs, batch_size=28, verbose=2)
