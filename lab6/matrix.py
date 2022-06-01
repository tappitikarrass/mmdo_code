class Matrix:
    def __init__(self, matrix, size_x, size_y):
        self.matrix = matrix
        self.size_x = size_x
        self.size_y = size_y

    def __str__(self):
        res = ""
        for i in range(len(self.matrix)):
            res += str(self.matrix[i]) + "\n"
        return res.strip()

class SquareMatrix(Matrix):
    def __init__(self, matrix, size):
        self.matrix = matrix
        self.size = size

    def __custom_min(self, lst, my_index):
        return min(x for idx, x in enumerate(lst) if idx != my_index)

    def __del_col_row(self, matrix, index1, index2):
        del matrix[index1]
        for i in matrix:
            del i[index2]
        return matrix

    def tsp(self):
        matrix = self.matrix
        data = self.size

        H = 0
        path_len= 0
        Str = []
        Stb = []
        res = []
        result = []
        intial_matrix = []

        # 0. fill arrays with indexes of available items
        for i in range(data):
            Str.append(i)
            Stb.append(i)

        for i in range(data):
            intial_matrix.append(matrix[i].copy())

        for i in range(data):
            matrix[i][i] = float('inf')

        while True:
            # 1. find minimal item in a row and substract from all other items
            for i in range(len(matrix)):
                buff = min(matrix[i])
                H += buff
                for j in range(len(matrix)):
                    matrix[i][j] -= buff
            
            # 2. find minimal item in a column and substract from all other items
            for i in range(len(matrix)):
                buff = min(row[i] for row in matrix)
                H += buff
                for j in range(len(matrix)):
                    matrix[j][i] -= buff
            

            # 3. find rank of all items equal zero;
            #    rank is sum of min item of row and column excluding current item
            max_rank = 0
            idx1, idx2 = 0, 0
            for i in range(len(matrix)):
                for j in range(len(matrix)):
                    if matrix[i][j] == 0:
                        cur_rank = (
                            self.__custom_min(matrix[i], j) +
                            self.__custom_min((row[j] for row in matrix), i)
                        )
                        if cur_rank >= max_rank:
                            max_rank = cur_rank
                            idx1 = i
                            idx2 = j

            # 3.5. add start and end indexes of the way to the array
            res.append(Str[idx1] + 1)
            res.append(Stb[idx2] + 1)
            old_idx1 = Str[idx1]
            old_idx2 = Stb[idx2]
            # 4. include way
            #    if way is still available, make unavailable;
            #    mark reverse way inf
            if old_idx2 in Str and old_idx1 in Stb:
                new_idx1 = Str.index(old_idx2)
                new_idx2 = Stb.index(old_idx1)
                matrix[new_idx1][new_idx2] = float('inf')

            del Str[idx1]
            del Stb[idx2]

            matrix = self.__del_col_row(matrix, idx1, idx2)
            # stop algo if all cols and rows except 1 was included
            if len(matrix) == 1:
                break

        
        # find the beggining of the path
        for i in range(0, len(res) - 1, 2):
            if res.count(res[i]) < 2:
                result.append(res[i])
                result.append(res[i + 1])

        # find all sequence of steps
        for i in range(0, len(res) - 1, 2):
            for j in range(0, len(res) - 1, 2):
                if result[len(result) - 1] == res[j]:
                    result.append(res[j])
                    result.append(res[j + 1])

        # find path length by summing values from initial matrix
        for i in range(0, len(result)-1,2):
            if i == len(result)-2:
                path_len += intial_matrix[result[i] - 1][result[i + 1] - 1]
                path_len += intial_matrix[result[i + 1] - 1][result[0] - 1]
            else:
                path_len += intial_matrix[result[i] - 1][result[i + 1] - 1]

        self.matrix = intial_matrix
        return result, path_len
