# Chapter 7 
# Programming Excercises 7.11
# Lo Shu Magic Square

# get rows and columns
def getRowsandColumns( user2DimensionalList ):
    numberOfRows = len( user2DimensionalList )
    numberOfColumns = ( len( user2DimensionalList[ 0 ] ) )

    return numberOfRows, numberOfColumns

# get sum of first row
def getFirstRowSum( user2DimensionalList, numberOfColumns ):
    firstRowSum = 0

    for currentRowIndex in range( 1 ):
        for currentColumnIndex in range( numberOfColumns ):
            firstRowSum = firstRowSum + user2DimensionalList[ currentRowIndex ][ currentColumnIndex ]

    return firstRowSum

# see if rows and sums equal
def hasEqualRowSums( user2DimensionalList, firstRowSum, numberOfRows, numberOfColumns ):
    rowSum = 0
    
    for currentRowIndex in range( numberOfRows ):
        for currentColumnIndex in range( numberOfColumns ):
            rowSum = rowSum + user2DimensionalList[ currentRowIndex ][ currentColumnIndex ]
        if rowSum != firstRowSum:
            return False
        rowSum = 0

    return True

# see if columns and sums equal
def hasEqualColumnSums( user2DimensionalList, firstRowSum, numberOfRows, numberOfColumns ):
    columnSum = 0
    
    for currentColumnIndex in range( numberOfColumns ):
        for currentRowIndex in range( numberOfRows ):
            columnSum = columnSum + user2DimensionalList[ currentRowIndex ][ currentColumnIndex ]
        if columnSum != firstRowSum:
            return False
        columnSum = 0

    return True

def hasEqualRowAndColumnSums( user2DimensionalList, firstRowSum,\
                              numberOfRows, numberOfColumns ):
    if hasEqualRowSums( user2DimensionalList, firstRowSum, numberOfRows, numberOfColumns ) and\
       hasEqualColumnSums( user2DimensionalList, firstRowSum, numberOfRows, numberOfColumns ):
        return True
    else:
        return False

def hasFromLeftEqualDiagonalSum( user2DimensionalList, lengthOfAnyRowOrColumn, ):
    fromLeftDiagonalSum = 0
    
    for currentDiagonalNumberIndex in range( lengthOfAnyRowOrColumn ):
        fromLeftDiagonalSum = fromLeftDiagonalSum +\
                              user2DimensionalList[ currentDiagonalNnumberIndex ]\
                              [ currentDiagonalNumberIndex ]
        
    if fromLeftDiagonalSum != firstRowSum:
        return False
    else:
        return True

def hasEqualFromRightDiagonalSum( user2DimensionalList, lengthOfAnyRowOrColumn, firstRowSum  ):
    fromRightDiagonalSum = 0
    currentDiagonalNumberColumnIndex = lengthOfAnyRowOrColumn - 1
    
    for currentDiagonalNumberRowIndex in range ( lengthOfAnyRowOrColumn ):
        fromRightDiagonalSum = fromRightDiagonalSum + user2DimensionalList[ currentDiagonalNumberRowIndex ][ currentDiagonalNumberColumnIndex ]
        currentDiagonalNumberColumnIndex = currentDiagonalNumberColumnIndex - 1

    if fromRightDiagonalSum != firstRowSum:
        return False
    else:
        return True

def hasEqualDiagonalSums( user2DimensionalList, lengthOfAnyRowOrColumn, firstRowSum ):
    if hasEqualFromRightDiagonalSum( user2DimensionalList,\
                                    lengthOfAnyRowOrColumn, firstRowSum ) and\
                                    hasEqualFromRightDiagonalSum( user2DimensionalList, lengthOfAnyRowOrColumn, firstRowSum ):
        
        return True
    else:
        return False

# see if list is a Lo Shu Magic Square
def isLoShuMagicSquare( user2DimensionalList, firstRowSum, numberOfRows, numberOfColumns, lengthOfAnyRowOrColumn ):
    if hasEqualRowAndColumnSums( user2DimensionalList, firstRowSum, \
                                 numberOfRows, numberOfColumns ) and\
                                 hasEqualDiagonalSums( user2DimensionalList, lengthOfAnyRowOrColumn, firstRowSum ):
        
        return True
    else:
        return False
    
# Create main function  
def main():
    user2DimensionalList = [
        [ 4, 9, 2 ],
        [ 3, 5, 7 ],
        [ 8, 1, 6 ]
    ]

    numberOfRows, numberOfColumns = getRowsandColumns( user2DimensionalList )

    lengthOfAnyRowOrColumn = numberOfRows

    firstRowSum = getFirstRowSum( user2DimensionalList, numberOfColumns )
    
    if isLoShuMagicSquare( user2DimensionalList, firstRowSum, numberOfRows, numberOfColumns, lengthOfAnyRowOrColumn  ):
        print( "This list is a Lo Shu Magic Square" )
    else:
        print( "This list is NOT a Lo Shu Magic Square" )

        
# Call main function
main()
               
    
