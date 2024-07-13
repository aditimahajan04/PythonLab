import numpy as np

# Read and display a 2D array
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original 2D Array:")
print(array)

# Display the array elements in reverse order
print("\nArray elements in reverse order:")
print(array[::-1, ::-1])

# Display all the elements of the principal diagonal elements
print("\nPrincipal diagonal elements:")
print(np.diag(array))

# Sort the 2D array in ascending order
print("\n2D Array sorted in ascending order:")
sorted_array = np.sort(array, axis=None).reshape(array.shape)
print(sorted_array)

# Sort the 2D array in descending order
print("\n2D Array sorted in descending order:")
sorted_array_desc = -np.sort(-array, axis=None).reshape(array.shape)
print(sorted_array_desc)
