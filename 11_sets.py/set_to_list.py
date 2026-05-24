empty_set = set()
print(type(empty_set))

empty_set = {"Yellow", "Blue", 1, 5, "Nepal"}
print(empty_set)

print(list(empty_set))


numbers = {5, 2, 9, 1, 2, 5}

# Convert set to list
numbers_list = list(numbers)

# Sort list
numbers_list.sort()

# Print sorted list
print("Sorted List:", numbers_list)

# Print length
print("Length:", len(numbers_list))