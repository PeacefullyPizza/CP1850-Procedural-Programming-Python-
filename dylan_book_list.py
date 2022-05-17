def main():
# Create empty list.
    total = []
#asks the user to enter totals for books.
    reportWriting = int(input("Enter the amount for Report Writing to add to the total: "))
    systemAnalysis = int(input("Enter the amount for System Analysis to add to the total: "))
    objectOriented = int(input("Enter the amount for Object Oriented Programming to add to the total: "))
    databaseDesign = int(input("Enter the amount for Database Design to add to the total: "))
    total.append( total )
#adds the book totals
    for total in range(len( total )):
                    bookTotal = reportWriting + systemAnalysis + objectOriented + databaseDesign
#after the loop ends it outputs the total
    print("The total of your books was:" + "\n$",str(bookTotal))

main()
