def check_discount(age, is_student):
    if age <= 12 or (age >= 13 and age <= 18):
        if is_student == "yes":
            print("You are eligible for a discount!")
        else:
            print("You are not eligible for any discount.")
    else:
        print("You are not eligible for any discount.")

def main():
    try:
        age= int(input("Enter your age: "))
        is_student = input("Are you a student? (yes/no): ").lower()
        if is_student != "yes" and is_student != "no":
            print("Invalid input for student status. Please enter 'yes' or 'no'.")
            return

        check_discount(age, is_student)
    except ValueError:
        print("Invalid input for age. Please enter a valid age.")

if __name__ == "__main__":
    main()