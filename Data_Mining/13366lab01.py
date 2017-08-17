import csv
import numpy as np

arr = []

def csvReader(file):
    """
    Read the given csv file to the array of "array"
    """
    reader = csv.reader(file)
    for element in reader:
        arr.append(element)


class Sn:
    def __init__(classObj, dataSet):
        classObj.dataSet = dataSet
	"""
	rather than using this all functions, we can just use inbuilt standered deviation
	function as "nympy.std()"
	"""
    def noOfElem(classObj, index):
        """
        get the number of elements in given column
        """
        return len(classObj.dataSet[:, index])

    def meanOf(classObj):
        """
        compute the mean of data set
        """
        return np.mean(classObj.dataSet, axis=0)	

    def diffSquaredSum(classObj ,dataSet, mean):
        """
        calculate Square sum of elements with difference of the mean value of the array
        """
        return np.sum((dataSet - mean)**2)		
		
    def getSn(classObj):
        """
        calculate the Sn value of the given datas
        """
        temp = []
        noOfColl = len(classObj.dataSet[0])
        mean = classObj.meanOf()
	#print(mean)
	#print(classObj.dataSet[:,2])

        for i in range(noOfColl):

            noOfElems = classObj.noOfElem(i)
			
            squareSum = classObj.diffSquaredSum(classObj.dataSet[:, i], mean[i])
            sn = np.sqrt(squareSum / (noOfElems - 1))
            temp.append(sn)

        return temp

		
if __name__ == "__main__":

    # Read CSV file
    csvPath = "labExercise01.csv"
    with open(csvPath, "rb") as fileObj:
        csvReader(fileObj)

    # Convert data into numpy array
    data = np.array(arr).astype(np.float_)

    # Calculate sN
    snObj = Sn(data)
    snList = snObj.getSn()
    print 'sN list : ', snList

			
		