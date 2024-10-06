#both single and double qoutes work
firstname = "Mark"
lastname = 'Henry'
print("Hello " + firstname + " " + lastname)

#you can use triple single or triple double qoutes
address = """
1 Main Street
Springfield
USA
"""
print("Address: " + address)

#escape douuble qoute 
print("Hello \"World\"")
#escape single qoute
print("Hello \'Word\'")

#concatination
print("Hello " + firstname + " " + lastname)

#string indexing
print("First letter of first name is " , firstname[0])
print("Second character of last name is " ,lastname[1])

#string slicing
alphabet = "abcdefghijklmnopqrstuvwxyz"

print("\nEntire Alphabet: " , alphabet[:] , " This syntax is same as: " , alphabet[0:len(alphabet)])

print("\nFirst 3 chars of alphabet: " , alphabet[0:3] , " This syntax is same as: " , alphabet[:3] )

print("\n2nd to 5th character: " , alphabet[2:5])

print("\nBoth this syntax give same result: " , alphabet[:-10] , " and " , alphabet[0:len(alphabet) - 10])

print("\nLast 10 chars of alphabet: " , alphabet[-10:] , "which is equal in syntax: " , alphabet[len(alphabet) -10 : len(alphabet)])

print("\nThis syntax: ", alphabet[-10:-3] , " is same as this syntax: " , alphabet[len(alphabet) -10 : len(alphabet) - 3])
