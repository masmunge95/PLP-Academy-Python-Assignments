# Creating a blank my_list
my_list = []

# Appending values to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f'Initial list after appending values: {my_list}') # Print list with appended values

# Insert 15 at index 1 (second position)
my_list.insert(1, 15)
print(f'List after inserting 15 at second position: {my_list}')

# Extend my_list with second_list
second_list = [50, 60, 70] # List to be used for extending
print(f'List to be used to extend: {second_list}') # show extension list 

my_list.extend(second_list) 
print(f'Updated list after extending: {my_list}') # Print list after extending 

# Remove the last element
my_list.remove(my_list[-1])
print(f'List after removing the last value: {my_list}')

# Sort the list
my_list.sort()
print(f'List after sorting: {my_list}')

# Find and print the index of 30
value_to_find = 30
if value_to_find in my_list:
    print(f' The value {value_to_find} is at index {my_list.index(value_to_find)} in the sorted list.')
else:
    print(f'The value {value_to_find} was not found in the list.')