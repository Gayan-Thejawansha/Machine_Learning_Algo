import csv
import numpy as np
import unittest
import pandas as pd
'''
@author E/13/366
Gayan S. Thejawansha
'''

class CM:
	def __init__(classObj, df , noOfVar ):
		classObj.noOfVar=noOfVar
		classObj.df=df
		
	def getCovMetrix(classObj):
		metrix = np.eye(classObj.noOfVar)
		for i in range(classObj.noOfVar):
			for j in range(i,classObj.noOfVar):
				metrix[i, j] = classObj.cov(classObj.df.iloc[:, i], classObj.df.iloc[:, j])
				metrix[j, i] = classObj.cov(classObj.df.iloc[:, i], classObj.df.iloc[:, j])
		return metrix		

	def cov(classObj,X,Y):
		N=len(X)
		sum=0.0
		Xbar=np.mean(X)
		Ybar=np.mean(Y)
		for index in range(0,N):
			sum=sum+(X[index]-Xbar)*(Y[index]-Ybar)
		return sum/(N-1)


	def getCorMetrix(classObj):
		metrix = np.eye(classObj.noOfVar)
		for i in range(classObj.noOfVar):
			for j in range(i,classObj.noOfVar):
				metrix[i, j] = classObj.cor(classObj.df.iloc[:, i], classObj.df.iloc[:, j])
				metrix[j, i] = classObj.cor(classObj.df.iloc[:, i], classObj.df.iloc[:, j])
		return metrix		
		
	def cor(classObj,X,Y):
		cov=classObj.cov(X,Y)
		sdX=classObj.std(X)
		sdY=classObj.std(Y)
		return cov/(sdX*sdY)
		
		
	def std(classObj,X):
		N=len(X)
		Xbar = np.mean(X)
		sum = 0.0
		for index in range(N):
			sum=sum + ((X[index] - Xbar)**2)
		
		var = sum/(N - 1)
		return np.sqrt(var)
		

class CMTest(unittest.TestCase):

	# df_1 = pd.Series([1,2,3,4,5])
	# df_2 = pd.Series([10,20,30,40,50])
	# df_3 = pd.Series([65,56,87,7,51])
	df_t = pd.Series([[1,2,3,4,5],[10,20,30,40,50],[65,56,87,7,51]])
	cm_t= CM(df_t,3)
	
	def setUp(classObj):
		print " test setup begin"

		
	def test_cov(classObj):
		
		cov_1 = CMTest.cm_t.cov(CMTest.df_t[0], CMTest.df_t[1])
		cov_2 = CMTest.cm_t.cov(CMTest.df_t[1], CMTest.df_t[2])		 
		classObj.assertEqual(np.around(cov_1, decimals=2), np.float64(25.0))
		classObj.assertEqual(np.around(cov_2, decimals=2), np.float64(-192.5))
		
	def test_cor(classObj):

		cor_1 = CMTest.cm_t.cor(CMTest.df_t[0], CMTest.df_t[1])
		cor_2 = CMTest.cm_t.cor(CMTest.df_t[1], CMTest.df_t[2])	
		classObj.assertEqual(np.around(cor_1, decimals=2), np.float64(1.0))
		classObj.assertEqual(np.around(cor_2, decimals=2), np.float64(-0.41999999999999998))
		
	def test_std(classObj):

		std_1 = CMTest.cm_t.std(CMTest.df_t[0])
		std_2 = CMTest.cm_t.std(CMTest.df_t[1])
		std_3 = CMTest.cm_t.std(CMTest.df_t[2])		 
		classObj.assertEqual(np.around(std_1, decimals=2), np.float64( 1.580000000000000))
		classObj.assertEqual(np.around(std_2, decimals=2), np.float64(15.81))
		classObj.assertEqual(np.around(std_3, decimals=2), np.float64(29.280000))
		
	def tearDown(classObj):
		print "test tearDown begin"					
		
if __name__ == "__main__":

	#read CSV and shaping
	df = pd.read_csv('lab03Exercise.csv',names = ['a','b','c', 'd','e'])
	df.shape
	#fill missing and not a number values
	#	df = df.fillna(df.mean())
	df = df.fillna(np.mean(df))
	cm = CM(df,5)
	# Find cov and correlation matrices
	cov = cm.getCovMetrix()
	cor = cm.getCorMetrix()
	print '---------- covarience ----------'
	print cov
	print '---------- correlation ----------'
	print cor
	unittest.main()
'''

2). As we can see in the reults, some value are over 0.9 while some are less than 0.5,
	we can see that highest corelation 1 is in between same data set and when the relativity become less the value become low.
	correlation 1 is in the same data set, [(1,1) , (2,2) , (3,3),(4,4),(5,5)]
	correlation > 0.7 have high relation than other values
        [ (1,2) , (1,3), (1,4), (2,3), (2,4), (3,4) ]  
	we can consider other collumns has les relativity.
	
3).  
'''	
	