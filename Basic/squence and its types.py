# what is squence in python
# A sequence is an ordered collection of items that can be indexed and iterated over.
# A sequence is a continuous memory allocation of data, where items are stored in memory in a linear manner.
# Types of sequence of three data types which are available in Python
# 1. List
# 2. Tuple
# 3. String
# 4. Range
# 5. Bytes

# Example of a list
my_list = [1, 2, 3, 4, 5]

# Example of a tuple
my_tuple = (1, 2, 3, 4, 5)

# Example of a string
my_string = "Hello, World!"

# Example of a range
my_range = range(1, 6)

# Example of bytes
my_bytes = bytes([1, 2, 3, 4, 5])

#what is string
# A string is a sequence of characters enclosed in quotes (single or double).
# Strings are immutable, meaning they cannot be changed after creation.
# immutable means that once a string is created, its content cannot be modified.

# Example of a single-line string
single_line_string = "This is a single-line string."
# Example of a multi-line string
multi_line_string = """This is a multi-line string.
It can span multiple lines.
"""
# Example of a string with line continuation
text = "Hello \
    world"

# Example of a multi-line string using triple quotes
txt = """This is a multi-line string.
It can span multiple lines.
"""

# Types of strings in Python
# 1. Single-line strings: Enclosed in single or double quotes, representing a single
#    line of text.
# 2. Multi-line strings: Enclosed in triple quotes, allowing for multiple lines of
#    text, which can include line breaks and indentation.
# 3. String with line continuation: Using a backslash (\) to continue a string on the next line.
# 4. Triple-quoted strings: Using triple quotes (single or double) to create strings that can span multiple lines.
# 5. Raw strings: Using the 'r' prefix to treat backslashes as literal characters, useful for regular expressions.
# 6. Unicode strings: Strings that can represent characters from various languages and scripts, using the 'u' prefix in Python 2 or simply as strings in Python 3.

#list
# A list is a sequence of items that is ordered and mutable.
# Lists are defined using square brackets [] and can contain items of different data types.
# Example of a list
my_list = [1, 2, 3, "Hello", True]
# Lists can be modified by adding, removing, or changing items.
# Example of modifying a list

# Tuples
# A tuple is a sequence of items that is ordered and immutable.
# Tuples are defined using parentheses () and can contain items of different data types.
# Example of a tuple
my_tuple = (1, 2, 3, "Hello", True)
# Tuples cannot be modified after creation, meaning you cannot add, remove, or change items.

tuple1 = (1, 2, 3, "Hello", True, "apple", "banana")
print(tuple1)


# what is mapping?
# A mapping is a collection of key-value pairs where each key is unique and maps to a specific value.
# In Python, mappings are implemented using dictionaries.
# key-value pair is the best thing to remember mapping and dictionary
# Example of a dictionary (mapping)
# key-value pairs are enclosed in curly brackets
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
 # dictionaries can be modified by adding, removing, or changing key-value pairs.
 # in dictionaries the value is mutable
 # (editable) but the key is immutable(not editable)

# Example of modifying a dictionary
my_dict["age"] = 31  # Changing the value of the key "age"
# Adding a new key-value pair
my_dict["country"] = "USA"  # Adding a new key-value pair
# Removing a key-value pair
del my_dict["city"]  # Removing the key "city"
# Example of accessing values in a dictionary
print(my_dict["name"])  # Accessing the value associated with the key "name"
