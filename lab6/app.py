from matrix import SquareMatrix

def print_path(result):
    result.append(result[0])
    for i in range(0,len(result), 2):
        if i == len(result) - 1:
            print('(',result[i-1],'-',result[i],')\n', end='')
        else:
            print('(', result[i], '-', result[i + 1], ') -> ', end='')

def main():
    matrix = [
        [0, 11, 5, 20, 5],
        [10, 0, 13, 5, 9],
        [11, 8, 0, 7, 17],
        [19, 15, 12, 0, 19],
        [10, 7, 18, 10, 0],
    ]
    A = SquareMatrix(matrix, len(matrix))
    print("Input matrix: ")
    print(A)
    print("Path: ", end="")
    result, path_len = A.tsp()
    print_path(result)
    print("Path len:", path_len)

if __name__ == "__main__":
    main()
