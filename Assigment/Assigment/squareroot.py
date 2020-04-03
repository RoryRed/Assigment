#Rory Redmond
#Write a program that takes a
# positive floating-point number as input and outputs an approximation of its square root. 
#You should create a function called sqrt that does this.

#formual x= 0.5(x+b/x)

#exponetial method

import numpy as np

def sqrt(number):#defining the function 
    a = float(number) #input number to get a sqrt of 
    for i in range(0,20000):# this repeats the steps inside the loop 2000 times 
        number = 0.5 * (number + a / number) #formula above
    return number,  #returns calculated number #retuening i also would result in the number of iterations taken to be displayes

y = float(input("enter any number : "))# enter any number you want the square root of 
y =round( y,1) # rounds number to one decimal place 
z = sqrt(y)
 # uses the defined function to get the square root
z =np.round( z,1)
print("the sqaure root of ", y , "is approximately " , z )#outputs result in format required 
# a type tuple error causes z to not round so numpy was imported to fix this 


#references
#http://danielhomola.com/2016/02/09/newtons-method-with-10-lines-of-python/
#https://www.youtube.com/watch?v=2GrfaB88w4M&t=168s
#https://pages.mtu.edu/~shene/COURSES/cs201/NOTES/chap06/sqrt-1.html
#https://www.youtube.com/watch?v=szQUIRPrAgQ