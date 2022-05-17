# Chapter 7 
# Programming Excercises 7.9
# Population Data

# Read Population data from file to list
def readPopulationDataFromFileToList( fileName ):
    populationDataFile = open( fileName, "r" )
    populationDataList = []

    populationForAYear = populationDataFile.readline()
    
    while populationForAYear != "":
        populationForAYear = int( populationForAYear )
        populationDataList.append( populationForAYear )
        populationForAYear = populationDataFile.readline()

    return populationDataList

# Calculate Population change
def calculatePopulationChange( populationDataList ):
    populationChangeDataList = []
    for populationForAYearIndex in range( len( populationDataList ) ):
        if populationForAYearIndex == 0:
            populationChangeDataList.append( 0 )
        else:
            populationChangeDataList.append( populationDataList[ populationForAYearIndex ] - \
                                             populationDataList[ populationForAYearIndex - 1 ] )
            
    return populationChangeDataList

# calculate average annual change 
def calculateAverageAnnualChangeInPopulation( populationChangeDataList ):
    totalPopulationChange = 0

    for populationChangeDataForAYearIndex in\
        range( len( populationChangeDataList ) ):
        totalPopulationChange = totalPopulationChange + populationChangeDataList[ populationChangeDataForAYearIndex ]

    averageAnnualChangeInPopulation = totalPopulationChange / len( populationChangeDataList )

    return averageAnnualChangeInPopulation

# calculate greatest increase in poplution for a year
def getGreatestIncreaseInPopulationYear( populationChangeDataList, startYear ):
    greatestIncreaseInPopulation = max( populationChangeDataList )

    greatestIncreaseInPopulationIndex = populationChangeDataList.index( greatestIncreaseInPopulation )

    greatestIncreaseInPopulationYear = greatestIncreaseInPopulation + startYear

    return greatestIncreaseInPopulationYear, greatestIncreaseInPopulation

# calculate smallest increase in poplution for a year        
def getSmallestIncreaseInPopulationYear( populationChangeDataList, startYear ):
    smallestIncreaseInPopulation = min( populationChangeDataList[ 1: ] )
    
    smallestIncreaseInPopulationIndex = populationChangeDataList.index( smallestIncreaseInPopulation )

    smallestIncreaseInPopulationYear = smallestIncreaseInPopulation + startYear
    
    return smallestIncreaseInPopulationYear, smallestIncreaseInPopulation

# Display population change data
def printYearsWithPopulationChangeData( populationChangeDataList, startYear ):
    for currentPopulationChangeDataForAYearIndex in range( len( populationChangeDataList ) ):
        
        currentYear = currentPopulationChangeDataForAYearIndex + startYear
        
        print( currentYear, " Had a population increase of", populationChangeDataList[ currentPopulationChangeDataForAYearIndex ] )
        
    print()

# display all data, Average change, greatest increase in year, greatest increase, smallest increase, smallest increase in year.    
def printPopulationData( averageAnnualChangeInPopulation, greatestIncreaseInPopulationYear,\
                         greatestIncreaseInPopulation, smallestIncreaseInPopulationYear,\
                         smallestIncreaseInPopulation, populationChangeDataList, startYear ):
    
    printYearsWithPopulationChangeData( populationChangeDataList, startYear )

    print( "The average annual change in population is " +\
           format( averageAnnualChangeInPopulation, ".2f" ), "The year with the greatest increase in population is " +\
           str( greatestIncreaseInPopulationYear ) +\
           " with a population of " + str( greatestIncreaseInPopulation ), \
           "The year with the smallest increase in population is" +\
           str( smallestIncreaseInPopulationYear ) +\
           " with a population of " + str( smallestIncreaseInPopulation ), \
           sep = "\n")

# Create main function
def main():
    fileName = "USPopulation.txt"

    START_YEAR = 1950
    
    populationDataList = readPopulationDataFromFileToList( fileName )

    populationChangeDataList = calculatePopulationChange( populationDataList )

    averageAnnualChangeInPopulation =\
                                    calculateAverageAnnualChangeInPopulation( populationChangeDataList )

    greatestIncreaseInPopulationYear, greatestIncreaseInPopulation =\
                                      getGreatestIncreaseInPopulationYear( populationChangeDataList, START_YEAR )

    smallestIncreaseInPopulationYear, smallestIncreaseInPopulation =\
                                      getSmallestIncreaseInPopulationYear( populationChangeDataList, START_YEAR )

    printPopulationData( averageAnnualChangeInPopulation, greatestIncreaseInPopulationYear,\
                         greatestIncreaseInPopulation, smallestIncreaseInPopulationYear,\
                         smallestIncreaseInPopulation, populationChangeDataList, START_YEAR )     
                                                                    
    
# Call main function
main()
               
    
