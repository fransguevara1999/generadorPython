#Clasificación Binaria

import pandas as pd
from keras.layers import Dense
from keras.models import Sequential
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

#Caragar datos
dataframe=pd.read_csv("Datasets/sonar.csv", header=None)
dataset=dataframe.values
print(dataset)

#Separación de caracteristicas con objetivo
X=dataset[:, 0:60].astype(float)
y=dataset[:, 60]
#print(X)
#print(y)
#label encoder
encoder=LabelEncoder()
encoder.fit(y)
encoder_y=encoder.transform(y)
#print(y)
#print(encoder_y)

def create_model():
    model=Sequential()
    model.add(Dense(60,input_dim=60,activation='relu'))
    model.add(Dense(30,activation='relu'))
    model.add(Dense(1,activation='sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

estimador=KerasClassifier(build_fn=create_model,epochs=100,batch_size=5,verbose=0)

kfold=StratifiedKFold(n_splits=10,shuffle=True)
result=cross_val_score(estimador,X,encoder_y,cv=kfold)
print("Linea Base: %.2f%% (%.2f%%)" % (result.mean()*100,result.std()*100))


#Optimizando Modelo
estimadores=[]
estimadores.append(('standarize',StandardScaler()))
estimadores.append(('mlp',KerasClassifier(build_fn=create_model,epochs=100,batch_size=5,verbose=0)))
pipeline=Pipeline(estimadores)
kfold=StratifiedKFold(n_splits=10,shuffle=True)
result=cross_val_score(pipeline,X,encoder_y,cv=kfold)
print("Modelo Estandarizado: %.2f%% (%.2f%%)" % (result.mean()*100,result.std()*100))