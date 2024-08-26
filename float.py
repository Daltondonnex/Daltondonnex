def find_greater_number():
    try:
        # Take two floating point numbers as input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Determine and print the greater number
        if num1 > num2:
            print(f"The greater number is: {num1}")
        elif num2 > num1:
            print(f"The greater number is: {num2}")
        else:
            print("Both numbers are equal.")
    except ValueError:
        print("Invalid input. Please enter valid floating-point numbers.")

# Call the function to test
find_greater_number()
