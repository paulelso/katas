# Description:  Function that takes a matrix (2D list) as input and 
# returns its transpose. 
# The transpose of a matrix switches its rows and columns.
def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(transpose(matrix))