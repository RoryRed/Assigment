import sys

f = open(sys.argv[1] ,"r")
j= f.read()
print(j.count("e"))

f.close()
