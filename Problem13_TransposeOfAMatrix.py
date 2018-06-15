def main():
    #For no of rows and columns
    rowsAndCols = raw_input()
    rowsAndCols = rowsAndCols.split(" ")
    rows_input,cols_input = int(rowsAndCols[0]),int(rowsAndCols[1])
    #declare matrix
    matrix1 = [[0 for x in range(cols_input)] for y in range(rows_input)]
    matrix2 = [0 for i in range(rows_input)]
    matrix3 = [[0 for x in range(rows_input)] for y in range(cols_input)]
    matrix4 = [0 for i in range(cols_input)]
    #For elements in matrix
    for i in range(0,rows_input):
        matrix2[i] = raw_input()
        newList = matrix2[i].split(" ")
        for k in range(0,len(newList)):
            matrix1[i][k]=int(newList[k])
    
    # Logic to convert matrix to its transpose
    for i in range(0,cols_input):
        for j in range(0,rows_input):
            matrix3[i][j] = matrix1[j][i]

    #print resultMatrix
    matrixRow = ''
    for i in range(0,cols_input):
        j=0
        for j in range(0,rows_input):
            if j <cols_input:
                matrixRow = matrixRow + str(matrix3[i][j]) + " " 
                j = j + 1
        print matrixRow
        matrixRow = ''
        i = i + 1 
        
main()