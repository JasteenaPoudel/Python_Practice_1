numbers = [5, 2, 9, 1]

print(sorted(numbers))
print(numbers)

print(numbers.sort())
print(numbers)



# sorted()

# Returns NEW sorted list.

# Original list unchanged.

# .sort()

# Changes original list.


#  REverse sorting
print(sorted(numbers, reverse=True))
print(numbers)

# Reverse List
print(numbers.reverse())
print(numbers)

# Method	 Changes Original List	   Returns Value
# sort()	 Yes.                 	    None
# reverse()	 Yes	                    None
# sorted()	 No	                        New sorted list