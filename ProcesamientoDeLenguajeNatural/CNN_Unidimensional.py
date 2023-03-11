
from keras.datasets import imdb
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Embedding
#from keras.preprocessing import sequence
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
from keras_preprocessing.sequence import pad_sequences

#Cargar Datos
vocal=5000
(X_train,y_train),(X_test,y_test)=imdb.load_data(num_words=vocal)
#Truncamiento de número máximo de palabras de la frase.
max_word=500
X_train=pad_sequences(X_train,maxlen=max_word)
X_test=pad_sequences(X_train,maxlen=max_word)
#Crear modelo de Red Neuronal 1D
model=Sequential()
model.add(Embedding(vocal,32,input_length=max_word))
model.add(Conv1D(32,3,padding='same',activation='relu'))
model.add(MaxPooling1D())

model.add(Flatten())
model.add(Dense(250,activation='relu'))
model.add(Dense(1,activation='sigmoid'))
#Compilacion
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
model.summary()

#Evaluar nuestro modelo
model.fit(X_train,y_train,validation_data=(X_test,y_test),epochs=2,batch_size=128,verbose=2)
#Final evaluado
scores=model.evaluate(X_test,y_test,verbose=0)
print('CNN Accuracy: %.2f%%' % (scores[1]*100))