# Задача 3.1.
# .
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - использовать готовые классы numpy.array() и pandas.DataFrame() запрещено!
#   - проявите фантазию :)

class Matrix:
    def __init__(self, row, column):
        self.matrix = self.get_matrix(row, column)
    def get_matrix(self, row, column):
        num = 1
        matrix = [[None for j in range(column)] for i in range(row)]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = num
                num += 1
        return matrix

    def get_matrix_str(self, matrix):
        strings = []
        for row in matrix:
            strings.append(str(row))
        return '\n'.join(strings)  
    def __str__(self):
        return self.get_matrix_str(self.matrix)
    def __len__(self):
        return len(self.matrix)
    def add(self, matrix):
        self.content.append(matrix)
    def get_rows_count(self):
        return self.row

    def get_columns_count(self):
        return self.column
           
m = Matrix(4, 5)
print(m)

1
# class Matrix:
#     def __init__(self, rows, columns):
#         self._matrix = [[None for j in range(columns)] for i in range(rows)]
#         self._rows = rows
#         self._columns = columns
    
#     def set_value(self, row, column, value):
#         self._matrix[row][column] = value
#     def get_value(self, row, column):
#         return self._matrix[row][column]
#     def get_rows_count(self):
#         return self._rows
#     def get_columns_count(self):
#         return self._columns
# m=Matrix(4, 4)
# for i in range(m.get_rows_count()):
#     for j in range(m.get_columns_count()):
#         m.set_value(i, j, 2)
# #print(m._matrix) #ни что-то он там страшное выдаст

# print(m._matrix)
#print(m._matrix[i])
#print(m._matrix[j])

# 0.0:
# for j in range(m.get_columns_count()):
2
# class Matrix:
#     def __init__(self):
#         self.matrix = []
#         self.rows = 0
#         self.columns = 0
        # content = None
        # content_type = type(content)

        #m=matrix(4,3)
       
#     content = 1
#     content_type = type(content)
#print()
# A1 = Cell()
# B2 = Cell()

# # Вызвать атрибуты экземпляра
# A1.content 
# print(A1.content)


# class Matrix2D:
#     def __init__(self):
#         '''
#         Init an empty matrix.
#         '''
#         self.matrix = []
#         self.rows = 0
#         self.columns = 0
#         self.name = 'Unnamed'

    # def __str__(self):
    #     return self.matrix

    # def generate(self, rows, columns, verbose=False):
    #     '''
    #     Return a list of lists containing the indices of the matrix (row, col)
    #     and prints it by row.
    #     int, int -> [[(int, int), ...], ...]
    #     '''
    #     self.rows = rows
    #     self.columns = columns
    #     self.matrix = [[(row, col) for col in range(columns)] for row in range(rows)]
    #     if verbose ==  True:
    #         print(f'Generated a {self.rows} row/s by {self.columns} column/s matrix')
    #         print('--------' * columns)
    #         self.printme()
    #         print('--------' * columns)
    #     return self.matrix

#     def printme(self, verbose=False):
#         '''
#         Print the matrix by row.
#         '''
#         if verbose == True:
#             print(f'I am a {self.rows} row/s by {self.columns} column/s matrix')
#         for row in self.matrix:
#             print(row)

#     def get_row(self, n, verbose=False):
#         '''
#         Return the row n of the matrix.
#         '''
#         if verbose ==  True:
#             print(f'matrix[row={n}]...')
#             print(self.matrix[n])
#         return self.matrix[n]

#     def get_col(self, n, verbose=False):
#         '''
#         Return the column n of the matrix.
#         '''
#         column_items = []
#         i = 0
#         while i < self.rows:
#             column_items.append(self.matrix[i][n])
#             i += 1
#         if verbose ==  True:
#             print(f'matrix[col={n}]...')
#             for item in column_items:
#                 print(item)
#         return column_items

#     def get_cell(self, row, col, verbose=False):
#         '''
#         Return a specific cell of the matrix.
#         '''
#         if verbose ==  True:
#             print(f'cell[row={row}, col={col}]...')
#             print(self.matrix[row][col])
#         return self.matrix[row][col]

#     def write_cell(self, row, col, data, verbose=False):
#         '''
#         Assign some data to a specific cell of the matrix.
#         '''
#         self.matrix[row][col] = data
#         if verbose ==  True:
#             print('Data wrote into cell[row={row}, col={col}]...')
#             print(self.matrix[row][col])                            
#         return self.matrix[row][col]
