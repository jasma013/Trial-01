from queue import LifoQueue

# Creating two instances
backward_history = LifoQueue()
forward_history = LifoQueue()
current_page = None

# Visit function
Noofvisits = int(input("Enter the number of URL history: "))
print("Enter URLs to visit:")
for i in range(Noofvisits):
    url = input("URL: ")
    print(f"Visiting {url}")
    backward_history.put(current_page)
    current_page = url
    # Display current page
    print(f"Current page: {current_page}")

# Go back
while input("Do you want to go back? (yes/no): ").lower() == "yes":
    if not backward_history.empty():
        forward_history.put(current_page)
        current_page = backward_history.get()
        print(f"Going back to {current_page}")
    else:
        print("No previous page available")
        break

# Go forward(reverse of backward)
while input("Do you want to go forward? (yes/no): ").lower() == "yes":
    if not forward_history.empty():
        backward_history.put(current_page)
        current_page = forward_history.get()
        print(f"Going forward to {current_page}")
    else:
        print("No forward page available")
        break