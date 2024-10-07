#literal pattern & wildcard(_)
grade = input("Enter your grade: ")

match grade:
  case 'A': 
    print("Excellent Grade")
  case 'B': 
    print("Good Grade") 
  case 'C': 
    print("Average Grade")
  case 'D': 
    print("Poor Grade")
  case _: 
    print("Invalid Grade")  


#variable pattern & gaurd classes
number = int(input("Enter a number: "))

match number:
  case x if x > 0: print("Positive number")
  case x if x < 0: print("Negative number")
  case 0: print("Zero") 

#combining patterns
light = input("Enter the color of the light: ")

match light.lower():
  case 'red' | 'yellow': print("Stop")
  case 'green': print("Go")
  case _: print(f"Invalid light colot: {light}")  

#sequence pattern
#tuple
#list

#dictionary pattern

#class pattern

    



