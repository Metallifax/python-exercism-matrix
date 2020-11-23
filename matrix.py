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
        new_arr = []
        for i in self.my_matrix[int(index-1),:]:
            new_arr.append(i)
        return new_arr

    def column(self, index):
        new_arr = []
        for i in self.my_matrix[:,[int(index-1)]]:
            new_arr.append(i)
        return new_arr

