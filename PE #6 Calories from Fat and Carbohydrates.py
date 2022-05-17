# Programming Exercises 6. Calories from Fat and Carbohydrates

# Calculate the Calories From Fat
def calculateCaloriesFromFat( fatGrams ):
    caloriesFromFat = fatGrams * 9
    return caloriesFromFat

# Calculate the Calories From Carbs
def calculateCaloriesFromCarbs( carbGrams ):
    caloriesFromCarbs = carbGrams * 4
    return caloriesFromCarbs

# Main function
def main():
    userFatGrams = float(input("Enter grams of fat:"))
    userCarbGrams = float(input("Enter grams of carbohydrates:"))
    caloriesFromFat = calculateCaloriesFromFat( userFatGrams )
    caloriesFromCarbs = calculateCaloriesFromCarbs( userCarbGrams )

    print("Calories From Fat: ", format(caloriesFromFat,",.2f"),"Calories From Carbs: ", format(caloriesFromCarbs,",.2f"))
    
main()
