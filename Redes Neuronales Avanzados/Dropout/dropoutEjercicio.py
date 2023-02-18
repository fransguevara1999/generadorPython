#importar librerias
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.optimizers import SGD
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
#Cargamos dataset
df=pd.read_csv("C:/dev/generadorPython/Datasets/sonar.csv",header=None)
df_values=df.values
#Separar X y y
X=df_values[:,0:60].astype(float)
y=df_values[:, 60]
#Esta codificada por lo que haces un encoder-De string a numerico
encoder=LabelEncoder()
encoder.fit(y)
encoder_y=encoder.transform(y)

#Como es un modelo de clasificacion nustro modelo debe estar creado como una función
def baseline_model():
    model=Sequential()
    model.add(Dense(60,input_dim=60,activation='relu'))
    model.add(Dense(30,activation='relu'))
    model.add(Dense(1,activation='sigmoid'))

    sgd=SGD(lr=0.01,momentum=0.8)
    model.compile(loss='binary_crossentropy',optimizer=sgd,metrics=['accuracy'])
    return model

#Result
estimador=[]
estimador.append(('standarize',StandardScaler()))
estimador.append(('MLP',KerasClassifier(build_fn=baseline_model,epochs=300,batch_size=16,verbose=0)))

pipeline=Pipeline(estimador)
kfold=StratifiedKFold(n_splits=10,shuffle=True)

result=cross_val_score(pipeline,X,encoder_y,cv=kfold)
print("Modelo de linea base: %.2f%% (%.2f%%)" % (result.mean()*100,result.std()*100))