print("Newton's Second Law of Motion")
print("------------------------------")
# Determine the missing value
print("Select the missing value:")
print("1. Mass (m)")
print("2. Acceleration (a)")
print("3. Force (F)")

missing_value_choice = input("Enter the option number for the missing value: ").strip()

# Prompt the user to enter the other two values based on the choice
try:
    if missing_value_choice == "1":
        # Calculate mass (m)
        a = float(input("Enter the acceleration (a): "))
        f = float(input("Enter the force (F): "))
        if a == 0:
            print("Acceleration cannot be zero.")
        else:
            m = f / a
            print(f"Mass (m) = {m:.2f}")
    elif missing_value_choice == "2":
        # Calculate acceleration (a)
        m = float(input("Enter the mass (m): "))
        f = float(input("Enter the force (F): "))
        if m == 0:
            print("Mass cannot be zero.")
        else:
            a = f / m
            print(f"Acceleration (a) = {a:.2f}")
    elif missing_value_choice == "3":
        # Calculate force (F)
        m = float(input("Enter the mass (m): "))
        a = float(input("Enter the acceleration (a): "))
        f = m * a
        print(f"Force (F) = {f:.2f}")
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
except ValueError:
    print("Invalid input. Please enter numerical values for mass, acceleration, and force.")
