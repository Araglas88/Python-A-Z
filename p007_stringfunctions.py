# Commonly used Python string functions

# len() - Returns the length of the string
text = "Python"
print(len(text))  # Output: 6

# upper() - Converts all characters to uppercase
print(text.upper())  # Output: PYTHON

# lower() - Converts all characters to lowercase
print(text.lower())  # Output: python

# strip() - Removes leading and trailing whitespace
text_with_spaces = "  Hello  "
print(text_with_spaces.strip())  # Output: Hello

# replace() - Replaces a substring with another substring
text = "Hello, World!"
print(text.replace("World", "Python"))  # Output: Hello, Python!

# split() - Splits a string into a list by a delimiter (default is space)
text = "Hello World"
print(text.split())  # Output: ['Hello', 'World']

# join() - Joins elements of a list into a single string with a delimiter
words = ['Hello', 'World']
print(" ".join(words))  # Output: Hello World

# startswith() - Returns True if the string starts with the specified prefix
print(text.startswith("Hello"))  # Output: True

# endswith() - Returns True if the string ends with the specified suffix
print(text.endswith("World"))  # Output: True

# find() - Returns the index of the first occurrence of a substring, -1 if not found
print(text.find("World"))  # Output: 6

# count() - Returns the number of occurrences of a substring
text = "banana"
print(text.count("a"))  # Output: 3

# capitalize() - Capitalizes the first character of the string
text = "python"
print(text.capitalize())  # Output: Python

# title() - Converts the first character of each word to uppercase
text = "hello world"
print(text.title())  # Output: Hello World

# isalpha() - Returns True if all characters are alphabetic
text = "Python"
print(text.isalpha())  # Output: True

# isdigit() - Returns True if all characters are digits
text = "12345"
print(text.isdigit())  # Output: True

# isalnum() - Returns True if all characters are alphanumeric
text = "Python3"
print(text.isalnum())  # Output: True

# isspace() - Returns True if the string contains only whitespace
text = "   "
print(text.isspace())  # Output: True

# lstrip() - Removes leading whitespace
text = "   Hello"
print(text.lstrip())  # Output: "Hello"

# rstrip() - Removes trailing whitespace
text = "Hello   "
print(text.rstrip())  # Output: "Hello"

# zfill() - Pads the string with zeros on the left until it reaches the specified width
text = "42"
print(text.zfill(5))  # Output: 00042

# partition() - Splits the string into three parts: before separator, separator, after separator
text = "Hello,World"
print(text.partition(","))  # Output: ('Hello', ',', 'World')

# rfind() - Finds the last occurrence of a substring
text = "Python programming"
print(text.rfind("o"))  # Output: 4

# rindex() - Finds the last occurrence of a substring, raises ValueError if not found
print(text.rindex("o"))  # Output: 4
