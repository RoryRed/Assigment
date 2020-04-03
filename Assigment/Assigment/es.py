#Rory Redmond
#import a file from an argument on the comand line.
#count the number of occurences of the letter "e"

import sys
 # allows an argument to passed from the command line to the script 
f = open(sys.argv[1] ,"r") #opens file to be read
j= f.read()           #reads the file 
print(j.count("e"))    # outputs the number of e's in the file
f.close()           # closes the file so other application can use the file

#references
#https://www.pythonforbeginners.com/system/python-sys-argv
