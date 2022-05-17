# Programming Exercise .6-12
# Average Steps Taken
month = ("January", "February", "March", "April", "May", "June", "July",
         "August", "September", "October", "November", "December")
days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
# Main Module
def main():
    # Call Header.
    header()
    # Call StepTracker.
    stepTracker()
# Header Module.
def header():
    # Display header
    print ("This is your step average for each month of the year:")
    print ("------------------------------------------------" \
            "--------------------")
# Counter Module.
def stepTracker():
    # This opens the steps.txt file.
    stepCounter = open('steps.txt', "r")
    # This sets the month count to zero.
    monthCount = 0
    # This loops through the months until the 12th month is reached.
    for num in range(1, 13):
        totalSteps = 0
        count = 0
        average = 0
        # This iterates until the end of the month is reached.
        for count in range(1, days[monthCount] + 1):
            # Reads lines until end.
            steps = int(stepCounter.readline())
            # Sum of the months.
            totalSteps = totalSteps + steps
        # This averages the steps for the month.
        average = totalSteps / days[monthCount]
        # Display average for month. 
        print ("The average steps taken for the month of " + month[monthCount] +
               " is: " + format(average, ",.1f") + " steps.")
        # This increments the months count
        monthCount = monthCount + 1
# Call main.
main()
