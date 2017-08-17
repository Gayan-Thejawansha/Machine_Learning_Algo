import csv
import numpy as np

rawData = []


def csv_reader(file_obj):
    """
    Read a csv file
    """
    reader = csv.reader(file_obj)
    for row in reader:
        rawData.append(row)


class Sn:
    def __init__(self, data_set):
        self.data_set = data_set

    def find_mean(self):
        """
        Find Mean of data set
        """
        return np.mean(self.data_set, axis=0)

    def find_no_of_elements(self, index):
        """
        Find no of elements in given column
        """
        return len(self.data_set[:, index])

    @staticmethod
    def find_square_sum(dataSet, mean):
        """
        Find Square sum of elements array
        """
        return np.sum((dataSet - mean)**2)

    def find_sn(self):
        """
        Find sN of given data set
        """
        temp = []
        no_of_columns = len(self.data_set[0])
        mean = self.find_mean()
	#print(mean)

        for i in range(no_of_columns):

            no_of_elements = self.find_no_of_elements(i)
            square_sum = self.find_square_sum(self.data_set[:, i], mean[i])
            sn = np.sqrt(square_sum / (no_of_elements - 1))
            temp.append(sn)

        return temp


if __name__ == "__main__":

    # Read CSV file
    csv_path = "labExercise01.csv"
    with open(csv_path, "rb") as f_obj:
        csv_reader(f_obj)

    # Convert data into numpy array
    data = np.array(rawData).astype(np.float_)

    # Calculate sN
    sn_obj = Sn(data)
    sn_list = sn_obj.find_sn()
    print 'sN list : ', sn_list

	