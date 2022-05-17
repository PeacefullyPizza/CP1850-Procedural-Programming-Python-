# Chapter 7 
# Programming Excercises 7.8
# Name Search

def readGirlsNamesFromFileToList( fileName ):
    girlsNamesFile = open( fileName, "r" )
    girlsNamesList = []

    girlName = girlsNamesFile.readline()

    while girlName != "":
        girlName = girlName.rstrip( "\n" )
        girlsNamesList.append( girlName )
        girlName = girlsNamesFile.readline()

    return girlsNamesList

def readBoysNamesFromFileToList( fileName ):
    boysNamesFile = open( fileName, "r" )
    boysNamesList = []

    boyName = boysNamesFile.readline()

    while boyName != "":
        boyName = boyName.rstrip( "\n" )
        boysNamesList.append( boyName )
        boyName = boysNamesFile.readline()

    return boysNamesList

def getUserSearchNames():
    userSearchName = input( "Please enter the first name to search for: ")
    userSearchNamesList = []
    
    while userSearchName != "-1":
        userSearchNamesList.append( userSearchName )
        userSearchName = input( "Please enter the next name to search for or -1 to continue: ")

    return userSearchNamesList

def searchForNames( userSearchNamesList, allNamesList ):
    foundNames = []
    
    for userSearchNamesListIndex in range( len( userSearchNamesList ) ):
        if userSearchNamesList[ userSearchNamesListIndex ] in allNamesList:
            foundNames.append( userSearchNamesList[ userSearchNamesListIndex ] )
        
    return foundNames

def printSearchResults( userSearchNamesList, foundNames ):
    for userSearchNamesListIndex in range( len( userSearchNamesList ) ):
        if userSearchNamesList[ userSearchNamesListIndex ] in foundNames:
            print()
            print( userSearchNamesList[ userSearchNamesListIndex ], "was found" )
        else:
            print( userSearchNamesList[ userSearchNamesListIndex ], "was not found" )
    

def main():
    girlsFileName = "GirlsNames.txt"
    boysFileName = "BoysNames.txt"
    
    girlsNamesList = readGirlsNamesFromFileToList( girlsFileName )
    
    boysNamesList = readBoysNamesFromFileToList( boysFileName )
    
    allNamesList = girlsNamesList + boysNamesList
    
    userSearchNamesList = getUserSearchNames()
    
    foundNamesList = searchForNames( userSearchNamesList, allNamesList )

    printSearchResults( userSearchNamesList, foundNamesList )
    
# Call main function
main()
               
    
