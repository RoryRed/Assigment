def sqrt(number, guess = 50000):#defining the function
    a = float(number) #input 
    for i in range(guess): 
        number = 0.5 * (number + a / number) 
	  
    return number 
y = float(input("enter any number : "))# enter any number you want the square root of 
y =round( y,1) # rounds number to one decimal place 
z = sqrt(y)# uses the defined function to get the square root
z = round( z, 1) rounds sqaure root to one decimal place 
print("the sqaure root of ", y , "is approximately " , z )#outputs result in format required 


#references
#http://danielhomola.com/2016/02/09/newtons-method-with-10-lines-of-python/
#https://www.youtube.com/watch?v=2GrfaB88w4M&t=168s
#