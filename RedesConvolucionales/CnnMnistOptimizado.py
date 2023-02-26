# Simple CNN for the MNIST Dataset
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.utils import np_utils

#cargar datos
(X_train,y_train),(X_test,y_test)=mnist.load_data()
X_train=X_train.reshape((X_train.shape[0],28,28,1)).astype('float32')
X_test=X_test.reshape((X_test.shape[0],28,28,1)).astype('float32')
print(X_test)
#Normalizamos los valores de los pixeles en el rango de 0 y 1 realizar OHE en el target
#Normalizar inputs para 0-255 yo 0-1
X_train=X_train/255
X_test=X_test/255
#One hot encode outputs
y_train=np_utils.to_categorical(y_train)
y_test=np_utils.to_categorical(y_test)
num_clases=y_test.shape[1]
#print(y_train)
print(num_clases)
#Define simple CNN
def larger_lineModel():
    #creacion de modelo
    model=Sequential()
    model.add(Conv2D(30,(5,5),input_shape=(28,28,1),activation='relu'))
    model.add(MaxPooling2D())
    model.add(Conv2D(15,(2,2),activation='relu'))
    model.add(MaxPooling2D())
    model.add(Dropout(0.2))
    model.add(Flatten())
    model.add(Dense(128,activation='relu'))
    model.add(Dense(150,activation='relu'))
    model.add(Dense(num_clases, activation='softmax'))
    #Compilar modelo
    model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
    return model

#Cargamos modelo
model=larger_lineModel()
#Fit de modelo
model.fit(X_train,y_train,validation_data=(X_test,y_test),epochs=10,batch_size=200)
#Evaluacion
score=model.evaluate(X_test,y_test,verbose=0)
print('Error de la CNN más profunda: %.2f%%' %(100-score[1]*100))
