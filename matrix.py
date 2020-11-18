class Matrix:
    def __init__(self, matrix_string):
        string = matrix_string
        arr = []
        for i in string:
            arr.append(i)
        self.mat_arr = arr
        self.mat_string = ''.join(arr)

    def __str__(self):
        return self.mat_string

    def get_arr(self):
        return self.mat_arr

    def get_str(self):
        return self.mat_string

    def get_parsed_arr(self):
        arr = self.get_arr()
        parsed_arr = []
        for i in range(len(arr)):
            if arr[i] == int:
                parsed_arr.append(arr[i])
            else:
                for j in range(len(parsed_arr)):
                    if int(arr[i][j]):
                        parsed_arr.append(arr[i][j])
        return parsed_arr


    def row(self, index):
        pass

    def column(self, index):
        pass

mat = Matrix('1 2 3 4\n5 6 7 8\n9 10 11 12')
print(mat)
print(mat.get_parsed_arr())