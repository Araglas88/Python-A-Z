#for on list
for i in ['good','bad','ugly']:
  print("List" , i)

#for on tuple
for i in ('good','bad','ugly'):
  print("Tuple" , i)

#for over set
for i in {2,3,4}:
  print("Set" , i)

#for on range
for i in range(1,5):
  print("Range",i)

#for on string
for i in "orange":
  print("String",i)

#for with enumerate
for index , color in enumerate(['red','yellow','green']):
  print(f"Index {index} is {color} ")

#for over dictionary

#for over zip
name = ['Boucher','Henry','Fiddle']
age = [23,24,25]

for n,a in zip(name,age):
  print(f"Name is {n} and age is {a}")

#for with else
for i in range(1,3):
  print(f"elserange {i}")
else:
  print("outside of for")

#for with try-except


