import pandas as pd
from keras.layers import Dense
from keras.models import Sequential
from keras.utils import np_utils
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder

dataframe = pd.read_csv("Datasets/iris.csv",delimiter=",", header=None)
dataset = dataframe.values
# print(dataset)
X = dataset[:, 0:4].astype(float)
y = dataset[:, 4]
print(X)
print(y)
encoder = LabelEncoder()
encoder.fit(y)
encoder_y = encoder.transform(y)
# print(encoder_y)
dummy_y = np_utils.to_categorical(encoder_y)
print(dummy_y)


# Definir nuestra red neuronal
def baseline_model():
    # Creacion de modelo
    model = Sequential()
    model.add(Dense(8, input_dim=4, activation='relu'))#4 entradas con 8 neuronas
    model.add(Dense(6, activation='relu'))
    model.add(Dense(3, activation='softmax'))
    # compilacion de modelo IMPORTANTE # Adam es gradiente descendiente
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    return model


# Definiendo clasificador
# Usaremos 200 epocas y 5 batch
estimador = KerasClassifier(build_fn=baseline_model, epochs=200, batch_size=5, verbose=0)
# Evaluamos nuestro modelo (estimador) en nuestro conjunto de datos(X e dummy_y). Utilizando el procedimiento
# de validación cruzada de 10 veces(kfold).
kfold = KFold(n_splits=10, shuffle=True)
result = cross_val_score(estimador, X, dummy_y, cv=kfold)
print("Accuracy: %.2f%% (%.2f%%)" % (result.mean() * 100, result.std() * 100))

