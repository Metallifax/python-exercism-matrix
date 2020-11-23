import numpy as np
from numpy import matrix, ndarray
import inspect
class Matrix: 
    def __init__(self,matrix_string):
        my_string = matrix_string.replace('\n', ';')
        self.matrix_string = ''.join(my_string)
        self.my_matrix = self.get_matrix()
        
    def get_matrix(self):
        return matrix(self.matrix_string)

    def __str__(self):
        return self.matrix_string

    def row(self, index):
        # Using Numpy more in depth
        my_arr = np.array(self.my_matrix)
        new_arr = []
        for i in my_arr[index - 1,:]:
            new_arr.append(i)
        return new_arr

        # Naive
        # new_arr = []
        # for i in self.my_matrix[int(index-1),:]:
        #     new_arr.append(i)
        # return ndarray.tolist(self.my_matrix[int(index-1),:])

    def column(self, index):
        my_arr = np.array(self.my_matrix)
        new_arr = []
        for i in my_arr[:,[index-1]]:
            new_arr.append(ndarray.item(i))
        return new_arr
        # new_arr = []
        # for i in self.my_matrix[:,[int(index-1)]]:
        #     new_arr.append(i)
        # return new_arr
