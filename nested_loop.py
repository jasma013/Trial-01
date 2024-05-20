# Loop through numbers from 1 to 19 (inclusive)
for i in range(1, 20):
    # Check if the current number is 3
    if i == 3:
        # Print a message indicating that 3 is being skipped
        print("Skipping 3 in the loop")
        # Skip the rest of the loop body for this iteration and move to the next iteration
        continue
    # Check if the current number is 7
    if i == 7:
        # Print a message indicating that the loop will break
        print("Reached 7, breaking the loop")
        # Exit the loop entirely
        break
    # Print the current number (this will be executed for all numbers except 3 and 7)
    print(i)
