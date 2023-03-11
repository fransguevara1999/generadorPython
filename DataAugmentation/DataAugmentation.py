from keras.datasets import mnist
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
#Cargar datos
(X_train,y_train),(X_test,y_test)=mnist.load_data()

#Reshape (Formato correcto para trabajar con imagenes)[n°total muestras que tenemos , ancho, alto y canales(blanco y negro es un canal)]
X_train=X_train.reshape((X_train.shape[0],28,28,1))
X_test=X_test.reshape((X_test.shape[0],28,28,1))
#Convertir las imagenes a flotante , porque estan en enteros.
X_train=X_train.astype('float32')
X_test=X_test.astype('float32')
#Preparacion de data
datagen=ImageDataGenerator(featurewise_center=True,featurewise_std_normalization=True)
#Entrenamiento
datagen.fit(X_train)
#Configure batch size
for X_batch,y_batch in datagen.flow(X_train,y_train,batch_size=9):
    for i in range(0,9):
        plt.subplot(330+1+i)
        plt.imshow(X_batch[i].reshape(28,28),cmap=plt.get_cmap('gray'))
    plt.show()
    break

