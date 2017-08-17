from sklearn import datasets
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
#import and make the instance of the data set
iris=datasets.load_iris()
#print the data set

print "##############################################################"
print " Print iris data set"
print iris
print "##############################################################"
print "\n \n \n"


X = iris.data[:, 3:4]
Y = iris.target


for i in range (len(Y)):
	if(Y[i]==2):
		Y[i]=1
	else:
		Y[i]=0
		
X.reshape(-1,1)	
#print X
#print Y

X_train , X_val , y_train , y_val = train_test_split(X, Y, test_size =0.2)
log_reg = LogisticRegression()
log_reg.fit(X_train , y_train)
y_proba = log_reg.predict(X_val)

print "##############################################################"
print "Logistic Regression"
print y_proba
print "##############################################################"
print "\n \n \n"
lin_reg = LinearRegression()
lin_reg.fit(X_train , y_train)
value = lin_reg.predict(X_val)
print "##############################################################"
print "Linear Regression"
print value
print "##############################################################"

