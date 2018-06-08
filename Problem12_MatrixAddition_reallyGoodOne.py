''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():

 # Write code here 
    rows1 = raw_input()
    listInput = rows1.split(" ")
    #print listInput
    rowsOfMatrices = int(listInput[0])
    columnsOfMatrices = int(listInput[1])
    # print rowsOfMatrices
    # print columnsOfMatrices
    rawLine = []

    matrix1 = [[0 for x in range(columnsOfMatrices)] for y in range(rowsOfMatrices)]
    
    resultMatrix = [[0 for x in range(columnsOfMatrices)] for y in range(rowsOfMatrices)]
    matrixCount = 0

    for i in range(0,rowsOfMatrices):
        newLine = raw_input()
        rawLine = newLine.split(" ")
        for j in range(0,columnsOfMatrices):
            valueToAppend = 0
            valueToAppend = int(rawLine[j])
            #print "Value to append:",valueToAppend
            matrix1[i][j]=valueToAppend
            #print "Matrix after this append:",matrix
            j = j + 1
        i = i + 1
        
    rows1 = raw_input()
    listInput = rows1.split(" ")
    #print listInput
    rowsOfMatrices = int(listInput[0])
    columnsOfMatrices = int(listInput[1])
    matrix2 = [[0 for x in range(columnsOfMatrices)] for y in range(rowsOfMatrices)]

    for i in range(0,rowsOfMatrices):
        newLine = raw_input()
        rawLine = newLine.split(" ")
        for j in range(0,columnsOfMatrices):
            valueToAppend = 0
            valueToAppend = int(rawLine[j])
            #print "Value to append:",valueToAppend
            matrix2[i][j]=valueToAppend
            #print "Matrix after this append:",matrix
            j = j + 1
        i = i + 1
    
    for i in range(0,rowsOfMatrices):
        for j in range(0,columnsOfMatrices):
            resultMatrix[i][j]=matrix1[i][j]+matrix2[i][j]
            j = j + 1
        i = i + 1
    #print resultMatrix
    matrixRow = ''
    for i in range(0,rowsOfMatrices):
        j=0
        for j in range(0,columnsOfMatrices):
            if j <columnsOfMatrices:
                matrixRow = matrixRow + str(resultMatrix[i][j]) + " " 
                j = j + 1
        print matrixRow
        matrixRow = ''
        i = i + 1
            
main()

