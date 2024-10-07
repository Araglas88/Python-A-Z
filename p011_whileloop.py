#basic while loop
i=3
while i <= 5:
  print("basic while ",i)
  i = i + 1

#while with else
i=2
while i <= 5:
  print("while + else",i)
  i = i +1
else: print("end of while")  

#while with break
i=1
while i <= 10:
  print("while + break " , i)
  if i == 5:
    break
  i = i + 1  
  

#while with continue
i=1
while i <= 10:
  i = i + 1
  if i ==3 or i==4:
    continue
  print("while + continue " , i)

#while with user input
while True:
  secret_code = input("Enter secret code: ")
  if secret_code == "secret":
    break

#while with try except

    