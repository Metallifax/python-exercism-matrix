from numpy import matrix

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
        return self.my_matrix[int(index),:]
    
    def my_column(self, index):
        return self.my_matrix[:,[int(index)]]

    def column(self, index):
        pass

mat = Matrix('1 2 3 4\n5 6 7 8\n9 10 11 12')
print(mat.my_matrix)
print(mat.row(0))
print(mat.my_column(0))