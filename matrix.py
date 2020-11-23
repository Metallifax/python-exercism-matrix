import numpy as np
from numpy import matrix, ndarray

class Matrix: 
    def __init__(self,matrix_string):
        # The secret sauce that turns the string into a viable np.matrix
        my_string = matrix_string.replace('\n', ';')
        self.matrix_string = ''.join(my_string)
        self.my_matrix = self.get_matrix()
        
    def get_matrix(self):
        # With this data structure I can parse rows and columns
        return matrix(self.matrix_string)

    def __str__(self):
        return self.matrix_string

    def row(self, index):
        # from matrix to ndArray type (numpy array)
        my_arr = np.array(self.my_matrix)
        # Using list comprehension to instantiate and assign ndArray items to new_arr.
        my_column = [x for x in my_arr[index-1,:]] 
        return my_column

    def column(self, index):
        # To ndArray (same as above)
        my_arr = np.array(self.my_matrix)
        # List comprehension again using python lists from ndArray
        my_row = [x for x in my_arr[:,[index-1]]]
        return my_row
