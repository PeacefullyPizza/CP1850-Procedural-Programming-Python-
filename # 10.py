# Chapter 7 
# Programming Excercises 7.10
# World Series Champions

# Open file to read to list
def readWinningTeamNamesFromFileToList( fileName ):
    winningTeamsFile = open( fileName, "r" )
    winningTeamsList = []
    
    winningTeam = winningTeamsFile.readline()

    # if there are no empty strings read next line
    while winningTeam != "":
        # strip newline corrector
        winningTeam = winningTeam.rstrip( "\n" )
        winningTeamsList.append( winningTeam )
        winningTeam = winningTeamsFile.readline()
    # Return Winning Teams List
    return winningTeamsList

# Get number of winning times
def getWinningTimes( userWinningTeamName, listOfWinningTeams ):
    winningTimes = 0

    for currentWinningTeamIndex in range( len( listOfWinningTeams ) ):
        if listOfWinningTeams[ currentWinningTeamIndex ] == userWinningTeamName:
            winningTimes = winningTimes + 1

    return winningTimes

# print function for displaying user searched team, and number of series won
def printWinningTimes( winningTeamName, winningTimes ):
    print( winningTeamName, "has won the World Series", winningTimes, "times" )

# main function
def main():
    fileName = "WorldSeriesWinners.txt"
    
    winningTeamsList = readWinningTeamNamesFromFileToList( fileName )

    userWinningTeamName = input( "Please enter the team name to search for: ")

    print()

    winningTimes = getWinningTimes( userWinningTeamName, winningTeamsList)

    printWinningTimes( userWinningTeamName, winningTimes )
    
# Call main function
main()
               
    
