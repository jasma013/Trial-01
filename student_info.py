# Initializing empty list and dictionary to store student information
students_list = []  # List to store student names
students_dict = {}  # Dictionary to store student details (name, age, grade)

# Function to add student information
def add_student():
    # Prompt user for student details
    name = input("Enter the student's name: ")
    age = int(input("Enter the student's age: "))
    grade = input("Enter student's grade: ")
    
    # Add student name to list and student details to dictionary
    students_list.append(name)
    students_dict[name] = {'age': age, 'grade': grade}
    print("Student's information added successfully.")

# Function to search for a student
def search_student():
    # Prompt user for student name to search
    name = input("Enter the student's name to search: ")
    
    # Check if student name exists in dictionary
    if name in students_dict:
        # If found, print student details
        print(f"Student's name: {name}")
        print(f"Age: {students_dict[name]['age']}")
        print(f"Grade: {students_dict[name]['grade']}")
    else:
        # If not found, display message
        print("Sorry, student not found.")

# Function to remove a student
def remove_student():
    # Prompt user for student name to remove
    name = input("Enter the student's name to remove: ")
    
    # Check if student name exists in list
    if name in students_list:
        # Remove student name from list and details from dictionary
        students_list.remove(name)
        del students_dict[name]
        print("Student removed successfully.")
    else:
        # If not found, display message
        print("Student not found.")

# Main program loop
while True:
    # Display menu options
    print("\nStudent Information Management System")
    print("1. Add student")
    print("2. Search student")
    print("3. Remove student")
    print("4. View all students")
    print("5. Exit")
    
    # Prompt user for choice
    choice = input("Enter your choice (1-5): ")
    
    # Process user's choice
    if choice == '1':
        add_student()
    elif choice == '2':
        search_student()
    elif choice == '3':
        remove_student()
    elif choice == '4':
        # Display all student details
        print("\nStudent Details:")
        for name, details in students_dict.items():
            print(f"Name: {name}, Age: {details['age']}, Grade: {details['grade']}")
    elif choice == '5':
        # Exit the program
        print("Exiting the program.")
        break
    else:
        # Invalid choice, prompt user to enter a number
        print("Invalid choice. Please enter a number.")
