
Rory Redmond
programming and scripting 

#task 2
bmi.py goal to 
calucate bmi giving the end user the ability to enter their own height and weight in si units  
used fromula for bmi provided 
inputs for weight and height were based of the tiles sample project 

#task 3

second string 
Goal:Write a program that takes asks a user to input a string and outputs every second letter in reverse order.
uses input method with string prompt.
created reversed variable
0 is where counting starts for the first character in the secetence 
100000 is large for the purpose of allowing much longer sentences to be resvered not just the prompt
2 is used to make it only count every second variable 

# task 4

collatz.py
goal:Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.
 At each step calculate the next value by taking the current value and, 
if it is even, divide it by two, but if it is odd, multiply it by three and add one.
Have the program end if the current value is one.
x is used for any given positive integer
y is defined as two to determine if its an even or odd number
while is used to create a loop that will end when x is equal to 1
x % y is used to see if a remainder is created.This allows the program to determine if the number is even or odd
if x is even it is devided by two.
else clause is used if a remainder is created from x%y
then the number is multiplied by 3 and 1.Brackets are not need as the order of operation is the desired outcome

task 5
weekday.py
Goal: Write a program that outputs whether or not today is a weekday
references :
https://www.programiz.com/python-programming/datetime/current-datetime
https://www.w3schools.com/php/php_ref_date.asp
datetime was imported 
the variable now was created which inputs the current day and time 
a diction was created which between 0-4 creates the response "Yes, unfortunately today is a weekday.
0-4 refers to monday to friday 
5 and 6 create the respone "Its is the weekend yay!"
5 and 6 refer to saturday and sundays
y uses the dictionary to get the approiate response for the current weekday
print(y) returns this response

task6 
square root.py	
Goal:Write a program that takes a positive floating-point number as input and outputs an approximation of its square root. 
You should create a function called sqrt that does this.

the easiest way to get the square root of a function in phyton is to create an input variable
eg x= float(input("Enter any number: ") 
z = round(x**0.5)
print(z)
squareroot.py
numpy was imported to resolve a type tuple error that occured when number of iteration was called 
creates a function  sqrt  the number is passed through the loop 20000 times this number was chosen to impove accuraccy 
line 18 and 19 allows the user to input a number that is then rounded to one decimal place
line 20 calls the function to act on the inputed number 
line 22 rounds that number to one decimal place 
line 23 output the square root and inital number in the desired form mat 



#return number exits the loop 



references
https://pages.mtu.edu/~shene/COURSES/cs201/NOTES/chap06/sqrt-1.html
#references
#http://danielhomola.com/2016/02/09/newtons-method-with-10-lines-of-python/
#https://www.youtube.com/watch?v=2GrfaB88w4M&t=168s
#https://pages.mtu.edu/~shene/COURSES/cs201/NOTES/chap06/sqrt-1.html
#https://www.youtube.com/watch?v=szQUIRPrAgQ


task 7
es.py 
goal :Write a program that reads in a text file and outputs the number of e's it contains. 
The program should take the filename from an argument on the command line.
import sys is used to allow the filename to be selected from an argument in the command line

sys argave contains the the comand line argument passed to the script
1 is used to represent the number of arguments.the open command opens the script
f.read reads the script
j.count counts the number of occurences of the letter e in the file 
f.close -closes the file

references
https://www.pythonforbeginners.com/system/python-sys-argv

task eight 
plot.py
goal:Write a program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
linspace sets a range of values 0 to 4 with 100 intervals

gx gives the square of x
hx gets the cube of x
plt.plot is used to plot x to the power of 1,2 and 3
plt.legend creates a legend with respect for each function with respect to there label
plt.xlabel titles the x axis 
plt.ylabel titles the y axis 
plt.show displays the graph
