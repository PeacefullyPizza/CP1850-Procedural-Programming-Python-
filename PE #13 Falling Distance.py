# Programming Exercises 13. Falling Distance

# Calculate The Falling Distance 
def fallingDistance( fallingTime ):
    gravity = 9.8
    distance = ( 1/ 2 ) * gravity * ( fallingTime ** 2 )
    return distance

# Display The Falling Distance in Range of 1 - 10
def main():
    print( "Time\tFalling Distance" )
    print( "----\t----------------" )
    for currentTime in range( 1, 11 ):
        print( currentTime,"\t", format( fallingDistance( currentTime ), ".2f")) 

main()
