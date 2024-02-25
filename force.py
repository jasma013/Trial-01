print("Newton's second law of motion")
print("------------------------------")
# Determine the missing value
print("Select the missing value:")
print("1. Mass (m)")
print("2. Acceleration (a)")
print("3. Force (F)")
missing_value_choice = input("Enter the option number or the missing value: ")
# Prompt the user to enter the other two values
if missing_value_choice == "1":
    a = float(input("Enter the acceleration (a): "))
    f = float(input("Enter force (F): "))
    m = f / a
    print(f"Mass (m) = {m}")
elif missing_value_choice == "2":
    m = float(input("Enter mass (m): "))
    f = float(input("Enter force (F): "))
    a = f / m
    print(f"Acceleration (a) = {a}")
elif missing_value_choice == "3":
    m = float(input("Enter mass (m): "))
    a = float(input("Enter acceleration (a): "))
    f = m * a
    print(f"Force (F) = {f}")
else:
    print("Invalid choice")








