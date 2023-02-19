import pandas as pd
from sklearn.utils import shuffle
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder

dataframe = pd.read_csv("Datasets/iris.csv", header=None)
dataset=dataframe.values
X=dataset[:, 0:4].astype(float)
y=dataset[:,4]

encoder= LabelEncoder()
encoder.fit(y)
encoded_y=encoder.transform(y)
print(encoded_y)

dummy_y=np_utils.to_categorical()
print(dummy_y)
