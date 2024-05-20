# Prompt the user to enter their name
identity = input("Please enter your name: ")

# Inform the user about the calculations
print("We will be calculating the sum, product, and quotient of two numbers you have entered.")

# Prompt the user to enter the first number
num_1 = float(input("Enter number 1: "))

# Prompt the user to enter the second number
num_2 = float(input("Enter number 2: "))

# Calculate the sum of the two numbers
sum_result = num_1 + num_2

# Calculate the product of the two numbers
product_result = num_1 * num_2

# Calculate the quotient of the two numbers, handle division by zero
if num_2 != 0:
    division_result = num_1 / num_2
else:
    division_result = "undefined (division by zero)"

# Print the results
print("Hello", identity, "Here are the results:")
print("The sum of the two numbers is:", sum_result)
print("The product of the two numbers is:", product_result)
print("The quotient of the two numbers is:", division_result)


