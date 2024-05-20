# Prompt the user to enter the number for which they want the multiplication table
num = int(input("Enter the number you want to get the multiplication table of: "))
print(f"Multiplication table of {num}:")

# Loop through numbers 1 to 12 to print the multiplication table
for i in range(1, 13):
    print(f"{num} x {i} = {num * i}")
