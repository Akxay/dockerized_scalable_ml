#Load required packages
import pandas as pd
import numpy as np
from sklearn.externals import joblib
from sklearn import svm, datasets
from sklearn.cross_validation import train_test_split, cross_val_score 
from sklearn.svm import SVC

iris = datasets.load_iris() # import data to play with
#print(iris.data.shape,iris.target.shape) #Print shape of data(Independent features) and target variable
#print ("Iris data set Description : ", iris['DESCR']) #To understand the data size, variables and class distribution
X = iris.data              #Features
y = iris.target             #Target variable

#split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)

#Using SVM classifier 
model = SVC(kernel='linear').fit(X_train, y_train) 
#Calculate Test Prediction
y_pred = model.predict(X_test)
print(model.score(X_test,y_test.ravel()))

# save model
joblib.dump(model, 'model/iris_svm_model.pkl', compress=True)

