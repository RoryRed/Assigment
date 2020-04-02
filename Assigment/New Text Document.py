def sqrt(number, guess = 500):
    a = float(number) 
    for i in range(guess): 
        number = 0.5 * (number + a / number) 
	  
    return number
y = float(input("enter any number : "))
y =round( y,1)
z = sqrt(y)
z = round( z, 1)
print("the sqaure root of ", y , "is approximately " , z )  