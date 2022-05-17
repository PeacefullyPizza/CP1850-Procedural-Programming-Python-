# Chapter 7 
# Programming Excercises 7.5
# Charge Account Validation

def getUserChargeAccountNumber():
    userChargeAccountNumber = input( "Please enter account number to search for: " )
    return userChargeAccountNumber

def readChargeAccountToList( chargeAccountsFile ):
    chargeAccountList = []
    chargeAccountNumber = chargeAccountsFile.readline()

    while chargeAccountNumber != "":
        chargeAccountNumber = chargeAccountNumber.rstrip( "\n" )
        chargeAccountList.append( chargeAccountNumber )
        chargeAccountNumber = chargeAccountsFile.readline()

    return chargeAccountList

def userChargeAccountNumberExists( userChargeAccountNumber, chargedAccountsList ):
    if userChargeAccountNumber in chargedAccountsList:
        return True
    else:
        return False


# Create the main function
def main():
    FILE_NAME = "charge_accounts.txt"
    
    chargeAccountsFile = open( FILE_NAME, "r" )
    
    chargeAccountsList = readChargeAccountToList( chargeAccountsFile )

    print( chargeAccountsList )

    userChargeAccountNumber = getUserChargeAccountNumber()
    if userChargeAccountNumberExists( userChargeAccountNumber, chargeAccountsList ):
       print( userChargeAccountNumber, "exists in", FILE_NAME )
    else:
        print( userChargeAccountNumber, "does not exist in", FILE_NAME )
        

# Call main function
main()
                           
    
