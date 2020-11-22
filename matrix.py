from numpy import matrix, array

class Matrix: 
    def __init__(self,matrix_string):
        my_string = matrix_string.replace('\n', ';')
        self.matrix_string = ''.join(my_string)
        
    def matrix_arr(self):
        return matrix(self.matrix_string)
    
    def __str__(self):
        return self.matrix_string

    def row(self, index):
        pass
    
    def column(self, index):
        pass

mat = Matrix('1 2 3 4\n5 6 7 8\n9 10 11 12')
print(mat)
print(mat.matrix_arr())