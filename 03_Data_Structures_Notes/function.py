'''what are the list
functions and methods in python
This script compares various list operations in Python, including joining, slicing, and replicating lists.
'''
# --- IGNORE ---
#list functions and methods in python
#length 
# function
def list_length(lst):
    return len(lst)
# list function
lst = [1, 2, 3, 4, 5]
l1 = list_length(lst)
print("Length of the list:", l1)  # Output: 5
t1 = (1, 2, 3, 4, 5, 6)
l1 = list(t1)
print("Length of the tuple:", l1)  # Output: 6

#lst.index(value) searches for the value in the list and returns its index.
lst = [1, 2, 3, 4, 5]
print("Index of 3 in the list:", lst.index(3))


#append function
lst = [1, 2, 3]
lst.append(4)
print (lst)


#extend function
lst1 = [1, 2, 3]
lst1.extend([4, 5, 6])  # Corrected 'extemh' to 'extend'
print("Extended List:", lst1)  # Output: [1, 2, 3, 4, 5, 6]


#insert function
lst = [1, 2, 3]
lst.insert(1, 4)  # Insert 4 at index 1
print("List after insertion:", lst)  # Output: [1, 4, 2, 3]

#pop function
lst = [1, 2, 3, 4, 5]
popped_element = lst.pop()  # Removes and returns the last element
print("Popped Element:", popped_element)  # Output: 5
# List after popping the last element
print("List after pop:", lst)  # Output: [1, 2, 3, 4]

#remove function
lst = [1, 2, 3, 4, 5]
lst.remove(3)  # Removes the first occurrence of 3
print("List after removing 3:", lst)  # Output: [1, 2, 4, 5]

#clear function
lst = [1, 2, 3, 4, 5]
lst.clear()  # Clears the list
print("List after clearing:", lst)  # Output: []
#copy function
lst = [1, 2, 3, 4, 5]
lst_copy = lst.copy()  # Creates a shallow copy of the list
print("Copied List:", lst_copy)  # Output: [1, 2, 3, 4, 5]

#sort function
lst = [5, 2, 3, 1, 4]
lst.sort()  # Sorts the list in ascending order
print("Sorted List:", lst)  # Output: [1, 2, 3, 4, 5]

#reverse function
lst = [1, 2, 3, 4, 5]
lst.reverse()  # Reverses the list in place
print("Reversed List:", lst)  # Output: [5, 4, 3, 2, 1]


#count function
lst = [1, 2, 3, 1, 2, 1]
count_1 = lst.count(1)  # Counts the occurrences of 1
print("Count of 1 in the list:", count_1)  # Output: 3

#reverser sort
lst = [5, 2, 3, 1, 4]
lst.sort(reverse=True)  # Sorts the list in descending order
print("Reversed Sorted List:", lst)  # Output: [5, 4, 3, 2, 1]

#min max sum function
lst = [1, 2, 3, 4, 5]
min_value = min(lst)  # Minimum value in the list
max_value = max(lst)  # Maximum value in the list
sum_value = sum(lst)  # Sum of all elements in the list
print("Min:", min_value)  # Output: 1
print("Max:", max_value)  # Output: 5
print("Sum:", sum_value)  # Output: 15
