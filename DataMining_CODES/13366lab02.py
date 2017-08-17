import csv
import numpy as np
import math
import matplotlib.pyplot as plt
import unittest

'''
@author E/13/366
Gayan S. Thejawansha
'''

class GD:
	def __init__(classObj, cur_x , precision , ler_rate ):
		classObj.cur_x=cur_x
		classObj.precision=precision
		classObj.ler_rate=ler_rate
		
	def deri_func(classObj, X):
		return 18*X*X -9

	def plot_function(classObj):
		x=np.linspace(-10,10,10000)
		function ='6*x**3-9*x+6'
		y=eval(function)
		plt.ylabel('f(X) value')
		plt.xlabel('X value')
		plt.plot(x,y)
		plt.show()

			
	def getGD(classObj):
		stepSize=classObj.precision + 100 
		'''stepSize value should not be initiate as current_x value, because the initial current_x value also can be initiate as large minus value'''
		while (stepSize> classObj.precision):
			prev_x=classObj.cur_x
			classObj.cur_x= classObj.cur_x - classObj.ler_rate*classObj.deri_func(classObj.cur_x)
			stepSize=math.fabs(classObj.cur_x-prev_x)
		return classObj.cur_x

class GDTest(unittest.TestCase):
	def setUp(self):
		print "gradient descent test setup begin"

		
	def test1(self):
		gd1=GD(1,1,0.1)
		self.assertEqual(gd1.getGD(), 0.09999999999999998)
		
	def test2(self):
		gd2=GD(1,2,0.1)	
		self.assertEqual(gd2.getGD(), 0.09999999999999998)
		
	def test3(self):
		gd3=GD(100,1,0.1)	
		self.assertEqual(gd3.getGD(),-float('inf'))
		
	def test4(self):
		gd4=GD(-100,1,0.1)
		self.assertEqual(gd4.getGD(),-float('inf'))
		
	def test5(self):
		gd5=GD(1,1,0.5)
		self.assertEqual(gd5.getGD(),-float('inf'))
		
	def test6(self):
		gd6=GD(1,1,0.05)
		self.assertEqual(gd6.getGD(),0.55)
		
	def tearDown(self):
		print "gradient descent test tearDown begin"					
		
if __name__ == "__main__":

	# Calculate
	gdObj =GD(100,1,0.05)
	gdObj.plot_function()
	gdValue = gdObj.getGD()
	print 'GD value : ', gdValue
	unittest.main()
'''
1). the behavior of f(x) is plotted

2). the initial value is a big factor to the algorithm to converge for the minimum value, as the plot indicates, when x goes
to minus infinity , f(x) goes its minimum ,that is minus infinity. but in some cases we can see that finite value get as the
answer. so that we can say the initial value has to chose carefully.

3). for the best results we must choose appropriate value for the learning rate. the parameter says how fast the algorithm 
converges to the answer. if it too large we may skip the optimal solution and if it too small it needs too many itterations to converge.

4). Here we can see that according to the plotted graph, the equation has a minimum in minus infinity. in many test cases it goees for the minus infinity,
but the value of d.f(x)/dx value becomes low, some of the answers could go error. 
'''	
	