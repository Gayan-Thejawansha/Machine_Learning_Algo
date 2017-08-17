import csv
import numpy as np
import pandas as pd

def cov(X,Y):
	N=len(X)
	sum=0.0
	Xbar=np.mean(X)
	Ybar=np.mean(Y)
	for index in range(0,N):
		sum=sum+(X[index]-Xbar)*(Y[index]-Ybar)
		#print sum

	return sum/(N-1)
	
df = pd.read_csv('lab03Exercise.csv',names = ['a','b','c', 'd','e'])
df.shape 
print "damn ",df.iloc[:, 1]
a=np.array(df['a'])
b=np.array(df['b'])
c=np.array(df['c'])
d=np.array(df['d'])
e=np.array(df['e'])
#aBar= np.mean(a)
aBar= np.mean(df['a'])
a[np.isnan(a)]=aBar

print cov(a,a)

print np.var(a)
print np.var(df['a'])