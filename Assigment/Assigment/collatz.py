#Rory Redmond
#check if the number is even or odd divide by two if even multiply by 3 and add 1 if odd
x = int(input("Please enter a positve integer: ")) 
y = 2 # used to to determine wether the number is even or odd
while x !=1: # stops when x = 1
  if x % y ==0: # no remainder when devided by two means the number is even 
    x = (x/y)
  else: # else is used here when the number is odd
    x = x*3 + 1
  print(x)




  