import numpy as np
from keras.callbacks import ModelCheckpoint
from keras.layers import Dense
from keras.models import Sequential

dataset = np.loadtxt("C:/dev/generadorPython/Datasets/pima-indians-diabetes.csv", delimiter=',')
X = dataset[:, 0:8]
y = dataset[:, 8]
# crear modelo
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
filepath = "weights-improvement-{epoch:02d}-{val_accuracy:0.2f}.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='val_accuracy', verbose=1, save_best_only=True, mode='max')
callbackList = [checkpoint]
model.fit(X, y, validation_split=0.33, epochs=150, batch_size=10, callbackList=callbackList, verbose=0)
