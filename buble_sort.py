def bubble_sort_2d(arr):
    # Get the number of rows and columns in the 2D array
    n = len(arr)
    m = len(arr[0])
    # Calculate the total number of elements in the 2D array
    total_elements = n * m

    # Perform bubble sort on the 2D array by treating it as a 1D array
    for i in range(total_elements - 1):
        # Each pass of bubble sort
        for j in range(total_elements - 1 - i):
            # Calculate the row and column for the current element
            row1 = j // m
            col1 = j % m

            # Calculate the row and column for the next element
            row2 = (j + 1) // m
            col2 = (j + 1) % m
            
            # Compare and swap if the current element is greater than the next element
            if arr[row1][col1] > arr[row2][col2]:
                # Swap elements
                arr[row1][col1], arr[row2][col2] = arr[row2][col2], arr[row1][col1]

    # Return the sorted 2D array
    return arr

# Example usage:
arr = [[5, 3, 2],
       [8, 6, 1],
       [4, 7, 9]]

# Sort the 2D array
sorted_arr = bubble_sort_2d(arr)

# Print the sorted 2D array
for row in sorted_arr:
    print(row)
