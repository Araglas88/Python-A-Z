#simple function
def printHello():
  print("Hello")

printHello()

#function with parameter
def printname(fnm,lnm):
  print("Hello ",fnm," ",lnm)

printname("Boucher","Mark")

#function with default value
def printdefaultname(fnm,lnm="Mark"):
  print("Hello "," " ,fnm," ",lnm)

printdefaultname("Melon")

#function with return
def retNum(num):
  return num

print(retNum(5))

#function with variable length arguments
def add(*multipleArgs):
  print(sum(multipleArgs))

add(1,2,3,4,5)

#function with keyword arguments
def student(**student_info):
  if "name" in student_info:
    print("Student name is " , student_info["name"])
  if "age" in student_info:
    print("Student age is " , student_info["age"]) 

student(name="Boucher",age=23)

#function with annotation
def add(x:int,y:int) -> int:
  return x+y

print(add(1,2))

#higher order function





  

  