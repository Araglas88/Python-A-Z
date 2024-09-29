fnm = input("Please enter first name: ")
lnm = input("Please enter last name: ")
print("Hello " + fnm + " " + lnm)

math_score = input(fnm + " " + lnm + " please input your matchs score:")
science_score = input(fnm + " " + lnm + " please input your science score:")

#we get wrong result
print(fnm, " " , lnm , " your total score is " , math_score + science_score ) 

#we get correct result
print(fnm , " " , lnm , " your total score is " , int(math_score) + int(science_score)) 

#you can convert while getting the input
float_num = float(input("enter a floating point number:"))
int_num = int(float_num)
print("floating point number is ", float_num , " which is converted to integer " , int_num)

#input always remember string type