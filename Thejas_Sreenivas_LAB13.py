
# Step-1: 
array = [[0] * 6 for _ in range(4)]

# Step-2: 
print("Shape of the array:", (len(array), len(array[0])))
print("Size of the array:", len(array) * len(array[0]))

# Step-3: 
new_row = [7] * len(array[0])  # Create a new row filled with 7s
array.insert(2, new_row)
print("After inserting a new row as the 3rd row:")
for row in array:
    print(row)

# Step-4: 
for row in array:
    row.insert(0, 2)   # Insert 2 at the beginning of each row
print("After inserting a new column as the 1st column:")
for row in array:
    print(row)

# Step-5: 
array.sort(key=lambda x: x)
print("After sorting the array row-wise:")
for row in array:
    print(row)

# Step-6: 
array = [row[:5] for row in array[:7]] #Resize the array to shape (7,5)
print("After resizing the array to shape (7,5) in row major order:")
for row in array:
    print(row)

# Step-7: 
flattened_array = [array[i][j] for j in range(len(array[0])) for i in range(len(array))]
print("Flattened array in column major order:")
print(flattened_array)

# Step-8: 
ones_array = [1] * 35  # Create a list of 35 ones
result = [a + b for a, b in zip(flattened_array, ones_array)]
print("Result after adding the ones array:")
print(result)
