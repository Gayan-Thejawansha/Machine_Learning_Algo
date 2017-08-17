# coding=utf-8
import numpy as np
import pandas as pd
import unittest


class DFLabTest(unittest.TestCase):
    ds_1 = pd.Series([5, 20, 40, 80, 100])
    ds_2 = pd.Series([10, 24, 33, 54, 10])
    ds_3 = pd.Series([5, 30, 10, 60, 50])

    def test_covariance(self):
        cov_1 = DFLab.covariance(DFLabTest.ds_1, DFLabTest.ds_2)
        cov_2 = DFLab.covariance(DFLabTest.ds_3, DFLabTest.ds_2)
        self.assertEqual(np.around(cov_1, decimals=2), np.float64(187.75))
        self.assertEqual(np.around(cov_2, decimals=2), np.float64(194.75))

    def test_correlation(self):
        cor_1 = DFLab.correlation(DFLabTest.ds_1, DFLabTest.ds_2)
        cor_2 = DFLab.correlation(DFLabTest.ds_3, DFLabTest.ds_2)
        self.assertEqual(np.around(cor_1, decimals=4), np.float64(0.2552))
        self.assertEqual(np.around(cor_2, decimals=4), np.float64(0.4404))

    def test_std(self):
        std_1 = DFLab.std(DFLabTest.ds_1)
        std_2 = DFLab.std(DFLabTest.ds_2)
        self.assertEqual(np.around(std_1, decimals=2), np.float64(40.06))
        self.assertEqual(np.around(std_2, decimals=2), np.float64(18.36))


class DFLab:
    def __init__(self, ds):
        self.ds = ds

    def findCovMatrix(self):
        cov_m = np.eye(5)
        for i in range(5):
            for j in range(i, 5):
                if i == j:
                    cov_m[i, j] = DFLab.covariance(self.ds.iloc[:, i], self.ds.iloc[:, i])
                else:
                    cov_m[i, j] = DFLab.covariance(self.ds.iloc[:, i], self.ds.iloc[:, j])
                    cov_m[j, i] = DFLab.covariance(self.ds.iloc[:, i], self.ds.iloc[:, j])
        return cov_m

    def findCorMatrix(self):
        cor_m = np.eye(5)
        for i in range(5):
            for j in range(i, 5):
                if i == j:
                    cor_m[i, j] = DFLab.correlation(self.ds.iloc[:, i], self.ds.iloc[:, i])
                else:
                    cor_m[i, j] = DFLab.correlation(self.ds.iloc[:, i], self.ds.iloc[:, j])
                    cor_m[j, i] = DFLab.correlation(self.ds.iloc[:, i], self.ds.iloc[:, j])
        return cor_m

    @staticmethod
    def covariance(X, Y):
        XMean = X.mean()
        YMean = Y.mean()
        covM = (((X - XMean) * (Y - YMean)).sum() / (X.count() - 1))
        return covM

    @staticmethod
    def correlation(X, Y):
        covM = DFLab.covariance(X, Y)
        sdX = DFLab.std(X)
        sdY = DFLab.std(Y)
        return covM/(sdX*sdY)

    @staticmethod
    def std(X):
        XMean = X.mean()
        var = ((X - XMean)**2).sum()/(X.count() - 1)
        return np.sqrt(var)

if __name__ == "__main__":
    # Read CSV
    df = pd.read_csv('lab03Exercise.csv', names = ['channel1', 'channel2', 'channel3', 'channel4', 'channel5'])
    print df
    # Fill missing values
    df = df.fillna(df.mean())
    # creating object
    DFLab = DFLab(df)
    # Find covariance and correlation matrices
    cov = DFLab.findCovMatrix()
    cor = DFLab.findCorMatrix()
    print '---------- covariance ----------'
    print cov
    print '---------- correlation ----------'
    print cor
    # Testing functions
    unittest.main()

'''
2 - ++  each value has highest correlation with each other(1) 
    ++  correlation that higher than 0.7 have high relation than other values
        (columns: (1,2) , (1,3), (1,4), (2,3), (2,4), (3,4) )  
    ++  A moderate correlation exists between the following columns.
        (columns: (2,5) , (3,5), (4,5) )
    ++ The correlation between the (1,5) is weak and it is the weakest of all correlations for the given matrix
'''

'''
3 -
The condition specified in section 1.3 does not divide the data into two classes. The conditions used, the mean values ​​
of the columns,The line does not change (it returns the same value regardless of the line being examined). The real 
state will be the condition Uses the values ​​in the string instead of the middle.
'''
