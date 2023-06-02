
import pandas as pd

dataset=pd.read_csv('https://raw.githubusercontent.com/mk-gurucharan/Classification/master/IrisDataset.csv')

X=dataset.iloc[:,:4].values
y=dataset['species'].values
print(dataset.head(5))

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

from sklearn.preprocessing import StandardScaler 
sc = StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)

from sklearn.naive_bayes import GaussianNB
classifier=GaussianNB()
classifier.fit(X_train,y_train)

#predicting y test set result
y_pred=classifier.predict(X_test)
y_pred

from sklearn.metrics import confusion_matrix 
cm = confusion_matrix(y_test,y_pred)

from sklearn.metrics import accuracy_score
print("Accuracy : ",accuracy_score(y_test,y_pred))
print(cm)

#compairing real value with predicted value
df=pd.DataFrame({'Real Values':y_test, 'Predicted Values':y_pred})
print(df)

from sklearn.metrics import precision_score,recall_score,accuracy_score

m=accuracy_score(y_test,y_pred)

print("Error Rate: ",1-m)

print("Precision: ",precision_score(y_test,y_pred,average='micro'))

print("Recall Score: ",recall_score(y_test,y_pred,average='micro'))




