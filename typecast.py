
#implicit type cast
a = 1
print("Type of a is " , type(a))
b = 2.5
print("Type of b is " , type(b))
c = a + b
print("Type of c is " , type(c) , "and value of c is", c)

#explicit type cast
a = "1"
print("Type of a is " , type(a))
b = 2
print("Type of b is " , type(b))
c = int(a) + b
print("Type of c is " , type(c) , "value of c is " , c)

#type cast functions
a = 3
print("value a " , a ," of " , type(a) , "is converted to float " , float(a) )
print("value a " , a ," of " , type(a) , "is converted to string " , str(a))
b = "5"
print("value b " , b ," of " , type(b) , "is converted to int " ,int(b))
c = 5.5
print("value c " , c ," of " , type(c) , "is converted to int " ,int(c))
d = [1,2,3]
print("value d " , d ," of " , type(d) , "is converted to tuple " ,tuple(d))
e = "123"
print("value e " , e ," of " , type(e) , "is converted to list " ,list(e))
print("value e " , e ," of " , type(e) , "is converted to tuple " ,tuple(e))

