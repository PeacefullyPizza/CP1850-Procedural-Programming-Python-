def main():
    try:
        gradesFile = open( "grades.txt" , "r")
        # Create variables.
        total = 0
        numberOfLines = 0
        line = gradesFile.readline()
        
        # Get total of grades from file.
        while line != "":
            numberOfLines += 1
            total += float( line )
            line = gradesFile.readline()  
        # Calculate the average of grades.
        average = total / numberOfLines
    # Display IOError if occured.    
    except IOError as error:
        print( "An IOError has occured", error)
    # Display ValueError if occured.    
    except ValueError as error:
        print( "A ValueError occured", error)
    else:
        # Display the average of the sum from the file.
        print( "\nThe average of grades in the file is" , "{:.2f}".format(average),"%")
    finally:
        print( "\nEnd of program" )
    
# Call main.
main()
