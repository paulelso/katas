# Description:  Function that takes a matrix (2D list) as input and 
# returns its transpose. 
# The transpose of a matrix switches its rows and columns.
def transpose(array):
    columns = len(array)
    for column in range(columns):
        rows = len(array[column])
        for row in range(rows):
            print(array[column][row])
    #array = [[array[j][i] for j in range(len(array))] for i in range(len(array[0]))]


if __name__ == "__main__":
    array = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    transpose(array)
